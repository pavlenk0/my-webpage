from django.db import models

class Article(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=100)
	text = models.TextField()

	def __str__(self):
			return self.title