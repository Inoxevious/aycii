from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q, F
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from account.models import *
import csv
from io import StringIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.http import HttpResponse, StreamingHttpResponse
from django.utils.text import slugify
# from account.models import *
from . models import *
def dept_detail(request,dept_id):
        totaldict = {}
        dept = Department.objects.get(id=dept_id)
        context = {
                'dept': dept,
        }
        return render(request, 'pages/dept_detail.html', context )

def notice_detail(request,notice_id):     
        totaldict = {}
        notice = NoticeBoard.objects.get(id=notice_id)
        context = {
                'notice': notice,
        }
        return render(request, 'pages/ay/components/notices/detail.html', context )


def article_detail(request,article_id):
        totaldict = {}
        article = Articles.objects.get(id=article_id)
        context = {
                'article': article,
        }
        return render(request, 'pages/ay/components/research/detail.html', context )


class HomePageView(TemplateView):
   
    template_name = 'pages/partials/home.html'

    def get_queryset(self, **kwargs):
        global object_list, paged_object_list
        object_list = AccountUser.objects.all()
        print('objet found',object_list)


        paginator = Paginator(object_list,3)
        page = self.request.GET.get('page')
        paged_object_list = paginator.get_page(page)


        return paged_object_list

def index(request):

    banners =  HomePageBanners.objects.all()
    global object_list, paged_object_list
    object_list = AccountUser.objects.all()
    print('objet found',object_list)

    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    paged_object_list = paginator.get_page(page)
    
    executive_dict = {}
    exe_statement_dict = {}
    appointment_date_dict = {}
    dept_dict = {}
    dept_id_dict = {}
    dep = object_list
    print('HOD FOUND',dep)
    for a in dep:
            try:
                    executive = Executive.objects.get(profile_id=a.id) 
                    print('active hot spot found ',Executive.id, ' ___', executive.role.name)
                    # exc_text = ExecutivesStatment.objects.get(author_id=executive.id)
                    executive_dict[executive.id] = []
                    executive_dict[executive.id].append(str(executive.role.name))
                    # exe_statement_dict[executive.id] = []
                    # exe_statement_dict[executive.id].append(str(exc_text.summary))
                    appointment_date_dict[executive.id] = []
                    appointment_date_dict[executive.id].append(executive.appointment_date)
                    dept_id_dict[executive.id] = []
                    dept_id_dict[executive.id].append(str(executive.dep.id))
                    dept_dict[executive.id] = []
                    dept_dict[executive.id].append(str(executive.dep.name))
            except (TypeError, ValueError, OverflowError, Executive.DoesNotExist):
                    dcost = 'Risk not added yet' 

    executive = Executive.objects.get(role=1)
    print('pres iddddddd................', executive.id)
    president = ExecutivesStatment.objects.get(author_id=executive.id)
    print('pres stt111111.................', president.summary)
    notices  = NoticeBoard.objects.all()   
    articles  = Articles.objects.all() 
    testimonials  = HomePageTestimonials.objects.all()
    events = Events.objects.all()
    depts = Department.objects.all()  
    context = { 'object_list': paged_object_list,
                'executive_role_dict': executive_dict,
                'appointment_date_dict': appointment_date_dict,
                'dept_dict': dept_dict,
                'dept_id_dict':dept_id_dict,
                'notices': notices,
                'articles': articles,
                'depts': depts,
                'banners': banners,
                'president': president,
                'testimonials':testimonials,
                'exe_statement_dict':exe_statement_dict,
                'events':events,
    
     }
    return render(request, 'pages/ay/index.html', context)

def guide(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/guide.html', context)

def contact(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/ay/components/contacts/contact.html', context)
def research(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/ay/components/research/research.html', context)
def about(request):
    testimonials  = HomePageTestimonials.objects.all()
    notices  = NoticeBoard.objects.all()
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
                'testimonials':testimonials,
                'notices': notices,
    
     }
    return render(request, 'pages/ay/components/about_us/about.html', context)
def business_portal(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
                'testimonials':testimonials,
    
     }
    return render(request, 'pages/ay/components/business_portal/portal.html', context)
def departments(request):
    articles  = Articles.objects.all()
    
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
                'articles': articles,
    
     }
    return render(request, 'pages/ay/components/departments/departments.html', context)
def events(request):
    depts = Department.objects.all() 
    events = Events.objects.all() 
    context = { 
                'depts': depts,
                'events':events,
    
     }
    return render(request, 'pages/ay/components/events/events.html', context)
def executives(request):
    executive = Executive.objects.get(role=1)
    print('pres iddddddd................', executive.id)
    president = ExecutivesStatment.objects.get(author_id=executive.id)
    testimonials  = HomePageTestimonials.objects.all()
    executives = ExecutivesStatment.objects.all()
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
                'president': president,
                'executives':executives,
                'testimonials':testimonials,
    
     }
    return render(request, 'pages/ay/components/executive/executives.html', context)

def members_portal(request):
    testimonials  = HomePageTestimonials.objects.all()
    notices  = NoticeBoard.objects.all()
    executive = Executive.objects.get(role=1)
    president = ExecutivesStatment.objects.get(author_id=executive.id)
    articles  = Articles.objects.all()
    depts = Department.objects.all()
    executives = ExecutivesStatment.objects.all()  
    context = { 
                'depts': depts,
                'testimonials':testimonials,
                'notices': notices,
                'executives':executives,
                'president': president,
                'articles': articles,
     }
    return render(request, 'pages/ay/components/members_portal/members_portal.html', context)

 
def faq(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/faq.html', context)