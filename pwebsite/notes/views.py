from django.shortcuts import render_to_response
from notes.models import Post, Category
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import Http404


#@login_required
def notes(request):
	posts = Post.objects.all().order_by('-submit_date')
	categories = Category.objects.all()
	return render_to_response('notes_home.html', {'posts':posts, 'categories':categories},context_instance=RequestContext(request))

def post(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404
	
	return render_to_response('notes_singelpost.html', {'post':post},context_instance=RequestContext(request))

def user_posts(request, username):

	searchstring = username
	try:
		user = User.objects.get(username=username)
		posts = Post.objects.all().filter(commited_by=user.id)
	except Post.DoesNotExist:
		raise Http404

	return render_to_response('notes_searchresults.html', {'searchstring':searchstring, 'posts':posts},context_instance=RequestContext(request))


def date_posts(request, day, month, year):

	day = int(day)
	month = int(month)
	year = int(year)
	
	posts = Post.objects.filter(submit_date__contains=datetime.date(year, month, day))
	searchstring = str(day) + "-" + str(month) + "-" + str(year)

	return render_to_response('notes_searchresults.html', {'searchstring':searchstring, 'posts':posts },context_instance=RequestContext(request))
