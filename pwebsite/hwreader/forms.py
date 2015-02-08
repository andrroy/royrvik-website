from django import forms

class LinkForm(forms.Form):
	link = forms.CharField(max_length=100)

def clean_message(self):
	return link