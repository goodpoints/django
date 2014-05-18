from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Organization(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255, null=True)
	city = models.CharField(max_length=255, null=True)
	state = models.CharField(max_length=255, null=True)
	zipcode = models.CharField(max_length=255, null=True)
	mission = models.CharField(max_length=255, null=True)
	phone = models.CharField(max_length=255, null=True)
	website_url = models.CharField(max_length=255, null=True)

	owner = models.ForeignKey(User)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	address = models.CharField(max_length=255, null=True)
	city = models.CharField(max_length=255, null=True)
	state = models.CharField(max_length=255, null=True)
	zipcode = models.CharField(max_length=255, null=True)
	avatar = models.CharField(max_length=255, null=True)
	organization = models.ForeignKey(Organization, null=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Venture(models.Model):
	organization = models.ForeignKey(Organization)
	name = models.CharField(max_length=255)
	description = models.TextField()
	impact_statement = models.CharField(max_length=255)
	video_url = models.CharField(max_length=255)
	image_url = models.CharField(max_length=255)
	impact_category = models.CharField(max_length=255)
	impact_objective = models.CharField(max_length=255)
	output_unit = models.CharField(max_length=255)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

class Milestone(models.Model):
	venture = models.ForeignKey(Venture)
	date = models.DateTimeField()
	unit = models.CharField(max_length=255)
	goal = models.FloatField()

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

class Campaign(models.Model):
	organization = models.ForeignKey(Organization)
	venture = models.ForeignKey(Venture)
	name = models.CharField(max_length=255)
	description = models.TextField()
	goal = models.FloatField()
	min_contribution = models.FloatField()
	end_date = models.DateTimeField()
	goal_met = models.BooleanField()
	paid_out = models.BooleanField()

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

class Receipt(models.Model):
	user = models.ForeignKey(User)
	campaign = models.ForeignKey(Campaign)
	date = models.DateTimeField()
	type = models.CharField(max_length=255)
	amount = models.FloatField(null=True)
	gp_received = models.FloatField()

