# Create your views here.
from django.shortcuts import render_to_response
from notes.models import Post
from django.template import RequestContext

def home(request):
	posts = Post.objects.all().order_by('-submit_date')

	if Post.objects.count() > 5:
		posts = Post.objects.all().order_by('-submit_date')[:5]

	authmsg = "Nope =/"
	if request.user.is_authenticated():
		authmsg = request.user.username


	return render_to_response('home.html', {'posts':posts, 'authmsg':authmsg}, context_instance=RequestContext(request))
