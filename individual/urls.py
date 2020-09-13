from django.conf.urls import url
from django.urls import path, include
from . import views 
# SET THE NAMESPACE!
app_name = 'individual'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    path('<int:user_id>/individual/', views.individual, name='individual'),
    path('home/', views.home, name='home'),
    path('profile_info/', views.profile_info, name='profile_info')

   
]