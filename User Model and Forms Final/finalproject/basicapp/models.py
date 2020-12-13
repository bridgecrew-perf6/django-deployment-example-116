from django.db import models
from django.contrib.auth.models import User



# Create your models here.

#We extends the User model and add additional attirbutes
class UserProfileInfo(models.Model):


	user = models.OneToOneField(User, on_delete = models.CASCADE,)

	#Additional attributes
	portfolio_site = models.URLField(blank = True)
	profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

	def __str__(self):
		return str(self.user)