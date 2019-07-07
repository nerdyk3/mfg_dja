from django.db import models


class blog(models.Model):
	Title = models.CharField(max_length=255)
	Description = models.CharField(max_length=255)
	content = models.TextField(max_length=255)
	def __str__(self):
		return ("%s | %s | %s")%(self.Title,self.Description,self.content)