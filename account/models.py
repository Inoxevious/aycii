from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class UserClass(models.Model): 
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=70)
    user_group = models.ForeignKey(UserClass, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
class MembershipClass(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name

class MembershipRole(models.Model):
    membership_class = models.ForeignKey(MembershipClass, on_delete = models.CASCADE)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
class Country(models.Model): 
    name = models.CharField(max_length=200, default='zim')
    official_language = models.TextField(null=True ,blank=True)
    flag = models.ImageField(null=True ,blank=True, upload_to='media/images/countries/flags')
    location = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
class AccountUser(models.Model):
    rmembership_role = models.ForeignKey(MembershipRole, on_delete = models.CASCADE,null=True ,blank=True,)
    age = models.IntegerField(null=True ,blank=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    address =models.TextField(null=True ,blank=True)
    date_birth =models.DateField(null=True ,blank=True)
    phone =models.CharField(null=True ,blank=True,max_length=70)
    id_number =models.CharField(null=True ,blank=True,max_length=20)
    gender =models.CharField(null=True ,blank=True,max_length=20)
    education_level =models.CharField(null=True ,blank=True,max_length=70)
    marital_status =models.CharField(null=True ,blank=True,max_length=20)
    number_dependants =models.IntegerField(null=True ,blank=True)
    total_worth =models.IntegerField(null=True ,blank=True)
    profile_pic = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    bio = models.TextField(null=True ,blank=True)
    country =  models.ForeignKey(Country, on_delete = models.CASCADE,null=True ,blank=True)
    

    def __str__(self):
        return self.user.username



class Department(models.Model):
    name = models.CharField(null=True ,blank=True,max_length=20)
    head = models.OneToOneField(AccountUser, on_delete = models.CASCADE)
    mission =models.TextField(null=True ,blank=True)
    vision =models.TextField(null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    def __str__(self):
        return self.name

class Executive(models.Model):
    profile = models.OneToOneField(AccountUser, on_delete = models.CASCADE)
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    role = models.ForeignKey(MembershipRole, on_delete = models.CASCADE)
    appointment_date = models.DateTimeField()
    valid_till_date = models.DateTimeField()
    def __str__(self):
        return self.profile.user.username

class NoticeBoard(models.Model):
    presidential = 'presidential'
    High = 'High'
    Medium = 'Medium'
    Low = "Low"
    malingoDalingo = 'malingoDalingo'
    PRIORITY_CHOICES = [
        (presidential,'presidential'),
        (High,'High'),
        (Medium,'Medium'),
        (Low,'Low'),
        (malingoDalingo,'malingoDalingo'),
    ]
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    priority = models.CharField(null=True ,blank=True,max_length=20, choices=PRIORITY_CHOICES, default = Low)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title =models.CharField(max_length=50,null=True ,blank=True)
    statement =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isFaceBanner = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title

class ExecutivesStatment(models.Model):
    author = models.ForeignKey(Executive, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title = models.CharField(max_length=50,null=True ,blank=True)
    summary =models.CharField(max_length=100,null=True ,blank=True)
    paragraph =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isHomeArticle = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title

class Articles(models.Model):
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    author = models.ForeignKey(AccountUser, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title =models.CharField(max_length=50,null=True ,blank=True)
    summary =models.CharField(max_length=100,null=True ,blank=True)
    paragraph =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isHomeArticle = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    def __str__(self):
        return self.title

class Events(models.Model):
    dep = models.ForeignKey(Department, on_delete = models.CASCADE)
    author = models.ForeignKey(AccountUser, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    video = models.FileField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    title =models.CharField(max_length=50,null=True ,blank=True)
    statement = models.TextField(null=True ,blank=True)
    event_link_zoom = models.TextField(null=True ,blank=True)
    event_link_teams =models.TextField(null=True ,blank=True)
    event_link_web =models.TextField(null=True ,blank=True)
    location =models.TextField(null=True ,blank=True)
    isActive = models.BooleanField(default=True)
    isFaceBanner = models.BooleanField(default=True)
    written_date = models.DateTimeField()
    published_date = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    def __str__(self):
        return self.title


