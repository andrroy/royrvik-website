from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=30, blank=False, null=False)

	class Meta:
		verbose_name="Category"
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=800, blank=False, null=False)
	content = models.TextField()
	commited_by = models.ForeignKey(User)
	submit_date = models.DateTimeField(auto_now_add=True, blank=True)
	category = models.ManyToManyField(Category)