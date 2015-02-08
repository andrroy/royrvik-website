from django.shortcuts import render_to_response
from django.template import RequestContext
from transfers.models import SC_Rating, Transfer_Post, RO_Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import json
from django.core import serializers
from django.http import HttpResponse

##################
##### Views ######
##################

# from django.views.decorators.csrf import csrf_exempt # Remove
@csrf_exempt # Remove
@login_required
def home(request):

	posts = Transfer_Post.objects.all()
	posts_to_be_displayed = 30

	if request.method == 'POST':

		data = get_new_articles(posts, posts_to_be_displayed, request)

		return HttpResponse(data, content_type="application/json")

	else:
		posts = posts.order_by('-id')[:posts_to_be_displayed]
		ratings = SC_Rating.objects.filter(post__in=posts)
		return render_to_response('transfers_home.html', {'posts':posts, 'ratings':ratings}, context_instance=RequestContext(request))

# Sumo view
@login_required
def sumo(request):
	posts = Transfer_Post.objects.all()
	ratings = SC_Rating.objects.all()
	return render_to_response('transfers_sumo.html', {'posts':posts, 'ratings':ratings}, context_instance=RequestContext(request))

# ITK RO section
@login_required
def itk_ro(request):
	ro_posts = RO_Post.objects.all().order_by('-id')
	if request.method == 'POST':
		data = get_new_ro_posts(ro_posts, request)
		return HttpResponse(data, content_type="application/json")
	else:
		return render_to_response('transfers_itk_ro.html', {'ro_posts':ro_posts}, context_instance=RequestContext(request))


@login_required
def info_screen(request):
	posts = Transfer_Post.objects.all()
	posts_to_be_displayed = 30

	if request.method == 'POST':

		data = get_new_articles(posts, posts_to_be_displayed, request)

		return HttpResponse(data, content_type="application/json")

	else:
		posts = posts.order_by('-id')[:posts_to_be_displayed]
		ratings = SC_Rating.objects.filter(post__in=posts)
		ro_posts = RO_Post.objects.all().order_by('-id')
		return render_to_response('transfers_infoscreen.html', {'posts':posts, 'ratings':ratings, 'ro_posts':ro_posts}, context_instance=RequestContext(request))





#############################
##### Helper functions ######
#############################
from django.core.serializers.json import DjangoJSONEncoder
def get_new_articles(posts, posts_to_be_displayed, request):
	# Get list of posts currently beeing displayed and convert to int
		post_ids = request.POST.getlist('post_ids[]')
		post_ids = map(int, post_ids)

		# If func == update_posts
		# Remove posts allready displayed, and old posts not to be displayed (Fix)

		if post_ids:
			for post in posts:
				if ( post.id < min(post_ids) ) or ( post.id in post_ids ):
					posts = posts.exclude(id=post.id)

		# Get corresponding ratings
		ratings = SC_Rating.objects.filter(post__in=posts)

		# Serialize / Convert to JSON
		posts_json = serializers.serialize('python',posts)
		ratings_json = serializers.serialize('python', ratings)

		data =  json.dumps( {'posts':posts_json, 'ratings':ratings_json}, cls=DjangoJSONEncoder )

		return data

def get_new_ro_posts(ro_posts, request):
	post_ids = request.POST.getlist('post_ids[]')
	post_ids = map(int, post_ids)

	for ro_post in ro_posts:
		if ro_post.id in post_ids:
			ro_posts = ro_posts.exclude(id=ro_post.id)

	ro_posts_json = serializers.serialize('python',ro_posts)

	data = json.dumps( {'ro_posts':ro_posts_json}, cls=DjangoJSONEncoder )

	return data

