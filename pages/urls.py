from django.conf.urls import url
from django.urls import path, include
from .views import *
# SET THE NAMESPACE!
app_name = 'pages'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('home', HomePageView.as_view(), name='home'),
    path('index/', index, name='index'),
    path('<int:notice_id>/notice_detail/', notice_detail, name='notice_detail'),
    path('<int:article_id>/article_detail/', article_detail, name='article_detail'),
    path('<int:dept_id>/dept_detail/', dept_detail, name='dept_detail'),
    # url(r'^dept_detail/$', dept_detail, name='dept_detail'),
    # path('register/', register, name='register'),
    path('guide/', guide, name='guide'),
    path('contact/', contact, name='contact'),
    path('research/', research, name='research'),
    path('about/', about, name='about'),
    path('executives/', executives, name='executives'),
    path('business_portal/', business_portal, name='business_portal'),
    path('members_portal/', members_portal, name='members_portal'),
    path('departments/', departments, name='departments'),
    path('events/', events, name='events'),
    path('faq/', faq, name='faq'),
   
]