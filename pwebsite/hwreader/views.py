from django.shortcuts import render_to_response

from hwreader.forms import LinkForm
from django.core.context_processors import csrf
from django.template import RequestContext

from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup
import re

def getContent(url):
	webpage = urlopen(url).read()

	patFinderTitle = re.compile('<title>(.*)</title>')
	patFinderParagraph = re.compile('<p>(.*)</p>')

	findPathTitle = re.findall(patFinderTitle,webpage)
	findPatParagraph = re.findall(patFinderParagraph,webpage)

	listIterator = []
	listIterator[:] = range(0,len(findPatParagraph)-8)

	content = "<h1>"
	content += findPathTitle[0]
	content += "</h1><br>"
	for i in listIterator:
		content += "<p>"
		content += findPatParagraph[i]
		content += "</p>"

	return content


def home(request):
	if request.method == 'POST':
		c = {}
		c.update(csrf(request))
		form = LinkForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			content = getContent(cd['link'])

			return render_to_response('hwreader_home.html', {'content':content})

	else:
		form = LinkForm()

	return render_to_response('hwreader_home.html', {'form':form}, context_instance=RequestContext(request))
