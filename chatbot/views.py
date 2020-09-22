from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# from products.models import Product
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchVector
from account.models import *
from django.contrib.auth.models import User
from django.db.models import Count
from django.conf import settings
# from cart.cart import Cart
from paynow import Paynow
from .models import PaynowPayment
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import datetime
import emoji
import random
import json
import time
import os

# Create your views here.
def generate_transaction_id():
    """
    Generates a unique id which will be used by paynow to refer to the payment
    initiated
    """
    return str(int(time.time() * 1000))


@csrf_exempt
def index(request):
    paynow = Paynow(
    '9437',
	'5f8250e8-1c59-4d2c-ba00-8bd74693e6c2',
    'http://example.com/gateways/paynow/update', 
    'http://example.com/return?gateway=paynow'
    )
    if request.method == 'POST':
        # retrieve incoming message from POST request in lowercase
        incoming_msg = request.POST['Body'].lower()
        # create Twilio XML response
        resp = MessagingResponse()
        msg = resp.message()
        
        responded = False

        if incoming_msg == 'hello':
            response = emoji.emojize("""
*Hello Comdrades! Welcome to AYCi Platform* :wave:
Let me assist you :wink:
You can type any of the following:
:black_small_square: *'executives':* To get a list of our executive board offices and phone numbers! :rocket:
:black_small_square: *'members':* To get a list of our members, country and phone numbers! :rocket:

:black_small_square:To register as a member:: register member*national id*name*surname*phone*email*gender*age*country*role# *e.g register member*29275558h26*innocent*mpasi#0777757603*mpasiinnocent@gmail.com*male*27*Zimbabwe*executive*# '*: On role write executive. If not an executive just add write non_executive.* 
""", use_aliases=True)
            msg.body(response)
            responded = True

        elif incoming_msg.startswith('register member'):
            result = ''

            # search for recipe based on user input (if empty, return featured recipes)
            search_text = incoming_msg.replace('register member', '')
            search_text = search_text.replace('*', ' ')
            search_text = search_text.replace('#', ' ')
            search_text = search_text.strip()
            text = str(search_text )
            national_id, name, surname, phone, email, gender, age, country, role, *_ = l = text.split()
            national_id = str(national_id)
            first_name = str(name)
            last_name = str(surname)
            phone = str(phone)
            email = str(email)
            gender = str(gender)
            age = int(age)
            country = str(country)
            role = str(role)
            if (national_id and role == 'non_executive'):
                request.session['national_id'] = national_id
                request.session['first_name'] = first_name
                request.session['last_name'] = last_name
                request.session['phone'] = phone
                request.session['email'] = email
                request.session['gender'] = gender
                request.session['country'] = country
                request.session['role'] = role
                request.session['age'] = age



                result += """

National ID: {}
Name:   {} 
Surname: {}
Phone: {}
""".format(national_id, name, surname, phone)
                result = 'Great, Is this correct National ID - *{}* Name- *{}* Surname- *{}* Phone *{}*. If Yes types "yes comrade"'.format(national_id, name,  surname, phone )

            elif (national_id and role == 'executive'):
                request.session['national_id'] = national_id
                request.session['first_name'] = first_name
                request.session['last_name'] = last_name
                request.session['phone'] = phone
                request.session['email'] = email
                request.session['gender'] = gender
                request.session['country'] = country
                request.session['age'] = age
                separator = ' - '
                s = Department.objects.all()
                num_dept = Department.objects.all().count()
                separator = ' - '
                if s:
                            result = ''

                            for dept in s:
                                dept_name = dept.name
                                dept_id = dept.id

                                result += """
    {}
    Department id:  {} 
    Department name:  {} 

    """.format(separator, dept_id, dept_name )

                else:
                    result = 'Sorry, I could not find any results'

                title = """*Select your department in this format, *select department*department_id#* e.g type 'select department*2#' for for media and news"""
                message = title + '\n'
                msg.body(message)
                msg.body(result)
                responded = True
            
            else:
                result = 'Sorry, I could not register member: {} of national ID: {} to database.'.format(name,  national_id )
            # image = str(image)
            # image = image.replace('/', "\\")
            # image = image.strip()
            # base = os.path.dirname(os.path.dirname(os.path.abspath(str(image))))
            # site_url = '127.0.0.1'
            # image = os.path.join(site_url + '/mush_store', image.url)
            # msg.media(image)
            
                msg.body(result)
                responded = True

        elif incoming_msg.startswith('select department'):
            result = ''
            search_text = incoming_msg.replace('select department', '')
            search_text = search_text.replace(' '' ', ' ')
            search_text = search_text.replace('*', ' ')
            search_text = search_text.replace('#', ' ')
            search_text = search_text.strip()
            text = str(search_text )
            department_id, *_ = l = text.split()

            department_id = str(department_id)

            request.session['department_id'] = department_id


            s = MembershipRole.objects.all()
            num_role = MembershipRole.objects.all().count()
            separator = ' - '
            if s:
                        result = ''

                        for role in s:
                            role_name = role.name
                            role_id = role.id
      

                            result += """
{}
dep id:  {} 
dep name:  {} 

""".format(separator, role_id, role_name )

            else:
                result = 'Sorry, I could not find any results'

            title = """*Select your role in this format, *select role*role_id#* eg 'select role*1#' for president """
            message = title + '\n'
            msg.body(message)
            msg.body(result)
            responded = True


        elif incoming_msg.startswith('select role'):
            result = ''
            search_text = incoming_msg.replace('select role', '')
            search_text = search_text.replace(' '' ', ' ')
            search_text = search_text.replace('*', ' ')
            search_text = search_text.replace('#', ' ')
            search_text = search_text.strip()
            text = str(search_text )
            role_id, *_ = l = text.split()
            role_id = str(role_id)
            request.session['role_id'] = role_id
            department_id = request.session['department_id']
            department = Department.objects.get(id=department_id)
            role = MembershipRole.objects.get(id=role_id)
            mrole= str(role.name)
            mdept = str(department.name)
            
            national_id = request.session['national_id']
            first_name = request.session['first_name']
            last_name = request.session['last_name']
            phone = request.session['phone']
            email = request.session['email']
            gender = request.session['gender']
            country = request.session['country']
            age = request.session['age']
            result += """

National ID: {}
First Name:   {} 
Last name: {}
Phone: {}
Email: {}
Gender: {}
Country: {}
Age: {}
Department: {}
Role: {}
""".format(national_id, first_name, last_name, phone, email, gender, country, age, mdept , mrole)
            result = 'Great, Is this correct National ID: *{}* Name: *{}* Last name: *{}* Phone: *{}* Email: *{}* Gender: *{}* Country: *{}* Age: *{}* Department: *{}* Role: {}. If Yes types "yes comrade"'.format(national_id, first_name,  last_name, phone, email, gender, country, age, mdept , mrole )

            msg.body(result)
            responded = True

        elif incoming_msg.startswith('yes comrade'):
            result = ''
            department_id = request.session['department_id']
            role_id = request.session['role_id'] 
            national_id = request.session['national_id']
            first_name = request.session['first_name']
            last_name = request.session['last_name']
            phone = request.session['phone']
            email = request.session['email']
            gender = request.session['gender']
            country = request.session['country'] 
            age = request.session['age']
            password = str(national_id)
            username = str(last_name + '-'+ first_name)
            # username = str(name) + str(surname)
            # Check username
            if User.objects.filter(email = email,username=username ).exists():
                result = 'Sorry, member: *{}* with national ID: {} is already registered.'.format(last_name,  national_id )
                # msg.body(result)
                # responded = True
            else :
                # looks good
                mrole =  MembershipRole.objects.get(id=role_id)
                mdept = Department.objects.get(id=department_id)
                print("ROLE Class", mrole.membership_class.name)
                if mrole.membership_class.name == 'executives':
                    user = User.objects.create_user(username = username,
                    password = password,email=email,first_name = first_name,
                    last_name = last_name, is_staff = True )
                    user.save()

                    user = get_object_or_404(User, email = email)  
                    acc = AccountUser(user_id = user.id, rmembership_role = mrole,phone = phone,gender=gender,country=country, age=age  )          
                    acc.save()
                    muser = AccountUser.objects.get(user_id = user.id)
                    exec = Executive(profile=muser, dep=mdept, role=mrole)
                    exec.save()
     
                    
                else:
                    user = User.objects.create_user(username = username,
                    password = password,email=email,first_name = first_name,
                    last_name = last_name )
                    user.save()

                    user = get_object_or_404(User, email = email)  
                    acc = AccountUser(user_id = user.id, rmembership_role = mrole )          
                    acc.save()

                result += """

Nationa ID: {}
Name:   {} 
Surname: {}
Phone: {}
""".format(national_id, first_name, last_name, country, phone)
                result = emoji.emojize("""
*Awesome progress Ambasaddor *{}* *{}* from *{}*  :wave:
*You are now a registered AYCi Member: with username (*{}*)*: 
:
:Your National : *{}* and  Phone numer *{}*. were added successfully.:
We appreciate you.:
: AYCi, enriching African youths.
""", use_aliases=True).format(first_name, last_name, country, username, national_id,phone )
                msg.body(result)
                responded = True

        elif incoming_msg == 'executives':
            s = Executive.objects.all()
            num_members = Executive.objects.all().count()
            separator = ' - '
            if s:
                        result = ''

                        for member in s:
                            first_name = member.profile.user.first_name
                            last_name = member.profile.user.last_name
                            country = member.profile.country
                            dep = member.dep.name
                            role = member.profile.rmembership_role.name
                            phone = member.profile.phone

                            result += """
{}
First Name:  {} 
Last Name:  {} 
Department: {}
Role:  {} 
Phone: *{}*
Country: {}
""".format(separator, first_name ,last_name,dep, role,phone, country )

            else:
                result = 'Sorry, I could not find any results'

            title = """*Number of Registered Members: ({})*""".format(num_members)
            message = title + '\n'
            msg.body(message)
            msg.body(result)
            responded = True

        elif incoming_msg == 'members':
            s = AccountUser.objects.all()
            num_members = AccountUser.objects.all().count()
            separator = ' - '
            if s:
                        result = ''

                        for member in s:
                            first_name = member.user.last_name
                            last_name = member.user.last_name
                            country = member.country
                            role = member.rmembership_role
                            phone = member.phone

                            result += """
{}
First Name:  {} 
Last Name:  {} 
Role:  {} 
Phone: *{}*
Country: {}
""".format(separator, first_name ,last_name,role,phone, country )

            else:
                result = 'Sorry, I could not find any results'

            title = """*Number of Registered Members: ({})*""".format(num_members)
            message = title + '\n'
            msg.body(message)
            msg.body(result)
            responded = True

        elif incoming_msg == 'departments':
            s = Department.objects.all()
            num_dept = Department.objects.all().count()
            separator = ' - '
            if s:
                        result = ''

                        for dept in s:
                            dept_name = dept.name
                            dept_id = dept.id
      

                            result += """
{}
dep id:  {} 
dep name:  {} 

""".format(separator, dept_id, dept_name )

            else:
                result = 'Sorry, I could not find any results'

            title = """*Number of Registered Roles: ({})*""".format(num_dept)
            message = title + '\n'
            msg.body(message)
            msg.body(result)
            responded = True

        elif incoming_msg == 'quote':
            # returns a quote
            r = requests.get('https://api.quotable.io/random')

            if r.status_code == 200:
                data = r.json()
                quote = f'{data["content"]} ({data["author"]})'

            else:
                quote = 'I could not retrieve a quote at this time, sorry.'

            msg.body(quote)
            responded = True

        elif incoming_msg == 'cat':
            # return a cat pic
            msg.media('https://cataas.com/cat')
            responded = True

        elif incoming_msg == 'dog':
            # return a dog pic
            r = requests.get('https://dog.ceo/api/breeds/image/random')
            data = r.json()
            msg.media(data['message'])
            responded = True

        

        elif incoming_msg.startswith('recipe'):

            # search for recipe based on user input (if empty, return featured recipes)
            search_text = incoming_msg.replace('recipe', '')
            search_text = search_text.strip()
            
            data = json.dumps({'searchText': search_text})
            
            result = ''
            # updates the Apify task input with user's search query
            r = requests.put('https://api.apify.com/v2/actor-tasks/o7PTf4BDcHhQbG7a2/input?token=qTt3H59g5qoWzesLWXeBKhsXu&ui=1', data = data, headers={"content-type": "application/json"})
            if r.status_code != 200:
                result = 'Sorry, I cannot search for recipes at this time.'

            # runs task to scrape Allrecipes for the top 5 search results
            r = requests.post('https://api.apify.com/v2/actor-tasks/o7PTf4BDcHhQbG7a2/runs?token=qTt3H59g5qoWzesLWXeBKhsXu&ui=1')
            if r.status_code != 201:
                result = 'Sorry, I cannot search Allrecipes.com at this time.'

            if not result:
                result = emoji.emojize("I am searching Allrecipes.com for the best {} recipes. :fork_and_knife:".format(search_text),
                                        use_aliases = True)
                result += "\nPlease wait for a few moments before typing 'get recipe' to get your recipes!"
            msg.body(result)
            responded = True

        elif incoming_msg == 'get recipe':
            # get the last run details
            r = requests.get('https://api.apify.com/v2/actor-tasks/o7PTf4BDcHhQbG7a2/runs/last?token=qTt3H59g5qoWzesLWXeBKhsXu')
            
            if r.status_code == 200:
                data = r.json()

                # check if last run has succeeded or is still running
                if data['data']['status'] == "RUNNING":
                    result = 'Sorry, your previous query is still running.'
                    result += "\nPlease wait for a few moments before typing 'get recipe' to get your recipes!"

                elif data['data']['status'] == "SUCCEEDED":

                    # get the last run dataset items
                    r = requests.get('https://api.apify.com/v2/actor-tasks/o7PTf4BDcHhQbG7a2/runs/last/dataset/items?token=qTt3H59g5qoWzesLWXeBKhsXu')
                    data = r.json()

                    if data:
                        result = ''

                        for recipe_data in data:
                            url = recipe_data['url']
                            name = recipe_data['name']
                            rating = recipe_data['rating']
                            rating_count = recipe_data['ratingcount']
                            prep = recipe_data['prep']
                            cook = recipe_data['cook']
                            ready_in = recipe_data['ready in']
                            calories = recipe_data['calories']

                            result += """
*{}*
_{} calories_
Rating: {:.2f} ({} ratings)
Prep: {}
Cook: {}
Ready in: {}
Recipe: {}
""".format(name, calories, float(rating), rating_count, prep, cook, ready_in, url)

                    else:
                        result = 'Sorry, I could not find any results for {}'.format(search_text)

                else:
                    result = 'Sorry, your previous search query has failed. Please try searching again.'

            else:
                result = 'I cannot retrieve recipes at this time. Sorry!'

            msg.body(result)
            responded = True

        elif incoming_msg == 'news':
            r = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news,the-washington-post,the-wall-street-journal,cnn,fox-news,cnbc,abc-news,business-insider-uk,google-news-uk,independent&apiKey=3ff5909978da49b68997fd2a1e21fae8')
            
            if r.status_code == 200:
                data = r.json()
                articles = data['articles'][:5]
                result = ''
                
                for article in articles:
                    title = article['title']
                    url = article['url']
                    if 'Z' in article['publishedAt']:
                        published_at = datetime.datetime.strptime(article['publishedAt'][:19], "%Y-%m-%dT%H:%M:%S")
                    else:
                        published_at = datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%S%z")
                    result += """
*{}*
Read more: {}
_Published at {:02}/{:02}/{:02} {:02}:{:02}:{:02} UTC_
""".format(
    title,
    url, 
    published_at.day, 
    published_at.month, 
    published_at.year, 
    published_at.hour, 
    published_at.minute, 
    published_at.second
    )

            else:
                result = 'I cannot fetch news at this time. Sorry!'

            msg.body(result)
            responded = True

        elif incoming_msg.startswith('meme'):
            r = requests.get('https://www.reddit.com/r/memes/top.json?limit=20?t=day', headers = {'User-agent': 'your bot 0.1'})
            
            if r.status_code == 200:
                data = r.json()
                memes = data['data']['children']
                random_meme = random.choice(memes)
                meme_data = random_meme['data']
                title = meme_data['title']
                image = meme_data['url']

                msg.body(title)
                msg.media(image)
            
            else:
                msg.body('Sorry, I cannot retrieve memes at this time.')

            responded = True

        if not responded:
             msg.body("Sorry, I don't understand. Send 'hello' for a list of commands.")

        return HttpResponse(str(resp))

    return HttpResponse('ok')
