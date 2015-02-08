## Parser module

from bs4 import BeautifulSoup
import urllib, urllib2, cookielib, re
from xml.sax import saxutils as su
import utilities

from models import SC_Rating, Transfer_Post, RO_Post

#
# Base functions
#

## Log in with session #####
def login(username, password):	
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	login_data = urllib.urlencode({'login' : username, 'password' : password})
	opener.open('http://spurscommunity.co.uk/index.php?login/login', login_data)
	return opener

## Sanitize html
def sanitize_html(value):
	INVALID_TAGS = ['div', 'article']
	soup = BeautifulSoup(value)

	#Remove inital blockquote
	for match in soup.findAll('blockquote', {'class', 'messageText'}):
		match.replaceWithChildren()

	# Remove invalid tags
	for tag in soup.findAll(True):
		if tag.name in INVALID_TAGS:
			tag.hidden = True

	return soup.renderContents()

#
# Functions spesific to daily thread
#

## Find link to current ITK thread
def get_current_itk_thread(opener):
	resp = opener.open('http://spurscommunity.co.uk/index.php?forums/transfer-rumours.46/index.rss')
	html = resp.read()

	soup = BeautifulSoup(html)

	threads = soup.findAll("item")

	for thread in threads:
		title = thread.find("title").string.lower()
		if ("daily itk" in title) or ("weekend itk" in title):
			return thread.find("link").string
	
	return "" # Fix this

## Parse current page
def parse_itk_thread(opener, link):
	# print "Initializing parsing on page %s" % link
	post_should_be_saved = False

	resp = opener.open(link)
	html = resp.read()

	soup = BeautifulSoup(html)

	# Find all posts
	posts = soup.findAll("li", { "class" : "message" })

	# Itterate every post
	for post in posts:
		poster = post.find('a', {'class': 'username'}) # Get user data
		content = post.findAll('article') # Get posts content
		ratings = post.findAll("ul", { "class" : "dark_postrating_outputlist" }) # Get ratings

		# Iterate ratings in post (Should be own function)
		for rating in ratings:
			s = BeautifulSoup(str(rating))
			for img in s.findAll('img'):
				if 'Informative' in img['alt']: # Keep it if post is rated informative
					post_should_be_saved = True

		# Save post if informative (saving should be own function)
		if(post_should_be_saved):
			raw_user_data =  utilities.fix_spurscommunity_url( str(poster) ) 
			raw_content_data = utilities.fix_spurscommunity_url( str(content) )

			# Start getting data to build object with
			poster = get_username( str(raw_user_data) )
			poster_url =  get_user_url( str(raw_user_data) )
			#Get context data
			context_poster, context_url, context_post, raw_content_data = get_context_data(raw_content_data)
			#Escape god damn unicode bs
			raw_content_data = su.unescape( raw_content_data ) 

			post_content =  str(raw_content_data).strip('[]')
			post_ratings = get_post_ratings( str(ratings) )

			# Sanitize 
			post_content = sanitize_html(post_content) # Change?
			if context_post:
				context_post = sanitize_html(context_post)
			# Save
			save_post( poster, poster_url, post_content, post_ratings, context_poster, context_post, context_url )
			# Reset
			post_should_be_saved = False

	# Get next page
	next_page = get_next_page(soup)

	if next_page:
		parse_itk_thread( opener, 'http://www.spurscommunity.co.uk/' + next_page )
	else:
		return link
			
## Get current page of thread
def get_current_page(soup):
	current_page = soup.find('a', { 'class': 'currentPage'})
	return current_page['href']

## Get next page of thread, return empty string if no found
def get_next_page(soup):
	page_nav = soup.find("div", {"class" : "PageNav"})
	try:
		for a in page_nav.findAll('a', { 'class': 'text'}):
			if 'Next' in a.string:
				return a['href']
		return ''
	except Exception:
		return ''

## Get username from html
def get_username(html):
	soup = BeautifulSoup(html)
	return soup.a.string

## Get url to user profile from html
def get_user_url(html):
	soup = BeautifulSoup(html)
	return soup.a.get('href')

## Get post ratings from html
def get_post_ratings(html):
	soup = BeautifulSoup(html)

	ratings = { '' : '' }

	for tag in soup.find_all( "li" ):
		try:
			ratings.update( { tag.img['alt'] : tag.strong.string } )
		except Exception:
			pass

	return ratings

## Gets all context data, and removes it from raw_data
def get_context_data(html):
	context_poster = ''
	context_url = ''
	context_post = ''

	soup = BeautifulSoup(html)

	for div in soup.find_all( "div", {"class": "bbCodeQuote"} ):
		if div.has_attr("data-author"): # Quote from user
			try:
				context_poster = div['data-author']
				context_url = soup.find('a', {'class' : 'AttributionLink'} )['href']
				context_post = soup.find('div', {'class': 'quote'}).string
				div.replaceWith('')
			except Exception:
				pass
		else: # Regular quote
			for quote in soup.findAll('div', {'class': 'quote'}):
				new_quote = '<blockquote>%s</blockquote>' % str( quote )
				div.replaceWith( new_quote )

	return context_poster, context_url, context_post, str(soup)



## Save daily post with ratings
def save_post(poster, poster_url, post_content, post_ratings, context_poster, context_post, context_url):
	obj, created = Transfer_Post.objects.get_or_create(poster = poster, poster_url = poster_url,
		context_url = context_url, context_post = context_post, context_poster = context_poster,
		post_content = post_content)

	for rating in post_ratings:
			if post_ratings[rating]:
				r, r_created = SC_Rating.objects.get_or_create( rating_type=rating, number_of=post_ratings[rating], post = obj )
				# Delete old foreign key if exists
				if r_created:
					SC_Rating.objects.filter(post__id=obj.id, rating_type=rating).delete() #Sorry
					r.save() #So sorry

#
# Functions spesific to ITK RO section
#

def parse_itk_ro_section(opener, feed):
	rss_feed = feed

	resp = opener.open(feed)
	html = resp.read()
	soup = BeautifulSoup(html)

	items = soup.findAll("item")

	for item in reversed(items):
		title = item.find('title').string
		post = item.find('content:encoded').string

		# Test
		s = BeautifulSoup(post)
		for tag in s.find_all( "div", {"class" : "quoteExpand"} ):
			tag.replaceWith('')

		post = str(s)
	
		# End
		save_ro_post(title, post)


def save_ro_post(t, p):
	obj, created = RO_Post.objects.get_or_create(title=t, content=p)

