from pwebsite import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pwebsite.settings")
from transfers import spurscommunity


def get_page_number_from_link(link):
	try:
		number = link.split("page-",1)[1]
		return number
	except Exception:
		return ''

def get_latest_news():
	# Get username and password
	username = settings.username
	password = settings.password

	# Login to sc
	opener = spurscommunity.login(username, password)

	# Get link to itk thread
	daily_thread = spurscommunity.get_current_itk_thread(opener)
	print "Get_latst_news parsing: %s" % daily_thread

	if daily_thread == settings.current_thread:
		link = settings.current_thread + "page-" + str(settings.current_page_number)
		new_link = spurscommunity.parse_itk_thread(opener, link)
		new_page_num = get_page_number_from_link(new_link)
		settings.current_page_number = new_page_num

	else:
		# Check if there are more post in last thread
		page = spurscommunity.parse_itk_thread(opener, str(daily_thread) )
		settings.current_page_number = get_page_number_from_link(page)
		settings.current_thread = daily_thread


# get_latest_news()

def update_ratings_in_daily():
	# Get username and password
	username = settings.username
	password = settings.password
	# Login to sc
	opener = spurscommunity.login(username, password)
	# Get link to itk thread
	daily_thread = spurscommunity.get_current_itk_thread(opener)
	print "Updating daily thread: %s" % daily_thread

	link = spurscommunity.parse_itk_thread(opener, daily_thread)
	print "Done"

# update_ratings_in_daily()

def update_itk_ro():
	# Get username and password
	username = settings.username
	password = settings.password
	# Login to sc
	opener = spurscommunity.login(username, password)

	spurscommunity.parse_itk_ro_section(opener, settings.itk_ro_feed)

update_itk_ro()

# Delete after use
def test():
	# Get username and password
	username = settings.username
	password = settings.password
	# Login to sc
	opener = spurscommunity.login(username, password)

	link = spurscommunity.parse_itk_thread(opener, 'http://spurscommunity.co.uk/index.php?threads/the-daily-itk-discussion-thread-21st-august-2014.111556/')

update_ratings_in_daily()



