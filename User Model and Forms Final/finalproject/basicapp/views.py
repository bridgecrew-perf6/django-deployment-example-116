from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

#Bult-in django decorators
from django.contrib.auth.decorators import login_required

#Built-in django authentication
from django.contrib.auth import authenticate, login, logout

#Importing the forms created
from basicapp.forms import UserForm, UserProfileInfoForm

#Importing models
from basicapp.models import UserProfileInfo

# Create your views here.

def index(request):
	return render(request, 'basicapp/index.html')


def register(request):
	registered = False

	if request.method == 'POST':
		#Create objects of type form
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileInfoForm(data = request.POST)

		#Check if the data entered is valid and then perform any action
		if user_form.is_valid() and profile_form.is_valid():
			#Variable USER which is an object of the instance UserForm saves the data submitted thru the form
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			#Check above as with USER. PROFILE is an object of type UserProfileInfoForm and has all the data submitted to the form inside and we can work with that data now.

			profile = profile_form.save(commit = False)

			#We can access USER with PROFILE, because PROFILE inharetes USER. Profile.User = User means that all data plus the new one will be saved.
			profile.user = user

			#Saving the picture uploaded by the user to the database

			if 'profile_pic' in request.FILES:
				profile_pic = request.FILES('profile_pic')

			profile.save()

			registered = True

		else:
			#Print registration errors
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	#Return the information acquired as dictionary to a template
	return render(request, 'basicapp/registration.html', {
		'user_form': user_form,
		'profile_form': profile_form,
		'registered': registered
		})


def user_login(request):
	#If the request is a POST we acquire the username and the password
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		#This will authenticate the user for us in one line of code
		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request, user)

				##If login is successful, user will be redirected to the home page
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse('User is not active')
		else:
			#If login was not successful, we will see it in the console with the code bellow
			print('Some one tried to login and failed')
			print('Username {} and Password {}'.format(username, password))
			return HttpResponse('Invalid login credentials')
	else:
		return render(request, 'basicapp/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
	user_list = UserProfileInfo.objects.order_by('user')
	return render(request, 'basicapp/special.html', {'users_list': user_list})







