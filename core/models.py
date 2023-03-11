from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from autoslug import AutoSlugField
User = get_user_model()

CATEGORIES = (
	('Science', 'Science'),
	('Art', 'Art'),
	('History', 'History'),
	('Technology', 'Technology'),
	('Business', 'Business'),

)

class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	id_user = models.IntegerField(null=True)
	phone_number = models.IntegerField(null=True)
	how_did_you_hear_about_us = models.TextField()
	what_will_you_use_paradox_for = models.TextField()

	def __str__(self):
		return self.user.username

class FlashCard(models.Model):
	title = models.CharField(max_length=999, unique=True, null=True)
	slug = AutoSlugField(populate_from="title", unique=True, null=True)
	featured_image = models.ImageField(upload_to="files/flashcard title images", null=True, help_text="upload an image with a resolution of 375x360")
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	description = models.TextField(null=True)
	category = models.CharField(max_length=400, choices=CATEGORIES, null=True )
	date_created = models.DateTimeField(null=True, auto_now_add=True)


	def __str__(self):
		return self.title

class Slide(models.Model):
	title = models.CharField(max_length=300, unique=True, null=True)
	description = models.TextField(null=True)
	flashcard = models.ForeignKey(FlashCard, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

# Create your models here.
