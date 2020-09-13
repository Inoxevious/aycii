# Create your models here.
from django.contrib.postgres.operations import TrigramExtension
from django.db import models,  migrations


class Migration(migrations.Migration):
  
    operations = [
        TrigramExtension(),
        
    ]
