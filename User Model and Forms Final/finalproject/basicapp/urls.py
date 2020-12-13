from django.urls import path
from basicapp import views




#app_name we are going to use for the templates

app_name = 'basicapp'



urlpatterns = [

    path('register/', views.register, name = 'user_register'),
    path('login/', views.user_login, name = 'user_login'),
    path('special/', views.special, name = 'special'),
    path('logout/', views.user_logout, name = 'user_logout'),


]