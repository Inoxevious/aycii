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
        return render(request, 'pages/partials/detail.html', context )


def article_detail(request,article_id):
        totaldict = {}
        articles = Articles.objects.get(id=article_id)
        context = {
                'articles': articles,
        }
        return render(request, 'pages/partials/article_detail.html', context )


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

    global object_list, paged_object_list
    object_list = AccountUser.objects.all()
    print('objet found',object_list)

    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    paged_object_list = paginator.get_page(page)
 
    executive_dict = {}
    appointment_date_dict = {}
    dept_dict = {}
    dept_id_dict = {}
    dep = object_list
    print('HOD FOUND',dep)
    for a in dep:
            try:
                    executive = Executive.objects.get(profile_id=a.id) 
                    print('active hot spot found ',Executive.id, ' ___', executive.role.name)
                    executive_dict[executive.id] = []
                    executive_dict[executive.id].append(str(executive.role.name))
                    appointment_date_dict[executive.id] = []
                    appointment_date_dict[executive.id].append(executive.appointment_date)
                    dept_id_dict[executive.id] = []
                    dept_id_dict[executive.id].append(str(executive.dep.id))
                    dept_dict[executive.id] = []
                    dept_dict[executive.id].append(str(executive.dep.name))
            except (TypeError, ValueError, OverflowError, Executive.DoesNotExist):
                    dcost = 'Risk not added yet'       

    notices  = NoticeBoard.objects.all()   
    articles  = Articles.objects.all() 
    depts = Department.objects.all()  
    context = { 'object_list': paged_object_list,
                'executive_role_dict': executive_dict,
                'appointment_date_dict': appointment_date_dict,
                'dept_dict': dept_dict,
                'dept_id_dict':dept_id_dict,
                'notices': notices,
                'articles': articles,
                'depts': depts,
    
     }
    return render(request, 'pages/home.html', context)

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
    return render(request, 'pages/contact.html', context)


def listing(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/listing.html', context)

# def loginn(request):
#     data = 'hie'
#     context = {'data':data}

#     return render(request, 'pages/login.html', context, context)

def primary(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }

    return render(request, 'pages/primary.html', context)

def secondary(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }

    return render(request, 'pages/secondary.html', context)

    
def faq(request):
    depts = Department.objects.all()  
    context = { 
                'depts': depts,
    
     }
    return render(request, 'pages/faq.html', context)