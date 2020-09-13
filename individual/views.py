from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db.models import Q
from account.models import AccountUser
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def individual(request, user_id):
    extra_context = ''
    title = ''
    fp = ''
    user = AccountUser.objects.get(user_id=user_id)
    print(user.user.username)

    # pdata = Product.objects.filter(short_name__icontains='maize')
    # # fproduce = fdata.farm_produce
    # for item in fdata:
    #     fp = item.farm_produce
    #     print(fp)
    # prd = ProductComposition.objects.filter(Q(composition__icontains=fp))
    # for item in prd:

    #     prd = item.product
    
    # prddata = Product.objects.filter(short_name__icontains=prd)
        

    # extra_context = extra_context or {'chart_data': chart_data, "testdata": testdata, "user":user}
    return render(request, 'farmer/home.html' )

def home(request):
    return render(request, 'farmer/home.html' )

def profile_info(request):
    return render(request, 'farmer/profile.html' )
