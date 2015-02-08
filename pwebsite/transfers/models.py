from django.db import models

class Transfer_Post(models.Model):
	poster = models.CharField(max_length=100)
	poster_url = models.CharField(max_length=500)
	context_url = models.CharField(max_length=500, null=True, blank=True)
	context_post = models.TextField(null=True, blank=True)
	context_poster = models.CharField(max_length=100, null=True, blank=True)
	post_content = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)

	class Meta:
		verbose_name="Transfer post"
		verbose_name_plural = 'Transfers posts'

class SC_Rating(models.Model):
	rating_type = models.CharField(max_length=100)
	number_of = models.IntegerField()
	post = models.ForeignKey(Transfer_Post)

	class Meta:
		verbose_name="Rating"
		verbose_name_plural = 'Ratings'


class RO_Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

	class Meta:
		verbose_name="RO post"
		verbose_name_plural = 'RO posts'