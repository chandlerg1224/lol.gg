from django.db import models
import string
import random
#models are the tables in the database. Django uses abstraction so we can code in python and 
#it gets translated into db commands
# Create your models here.
#fat models and this views, put most of your logic on your models


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        #filter all room objects with the code that was generated
        #we count the number of objects with the same code that we generated
        #if this count is 0, then we got a unique code and we can break out of the loop
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


class Room(models.Model):
    #field with constraints relating to this code field, length = 8, default nothing, unique chars
    code = models.CharField(max_length=8, default ="", unique=True)
    #stores the info relating to the host of the room/who the host is
    host = models.CharField(max_length=50, unique=True)
    #null=false means a value must be passed
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    #auto now add automatically adds the date and time of creation
    created_at = models.DateTimeField(auto_now_add=True)
    
    