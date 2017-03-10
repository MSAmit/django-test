from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	createdDate = models.DateTimeField()
	tags = TaggableManager()
	
	def __unicode__(self):
		return self.title