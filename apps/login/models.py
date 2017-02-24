from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import datetime, timedelta
import re, bcrypt

class UserManager(models.Manager):
    def validation(self, postData):
        errors=[]
        if len(postData["name"])==0:
            errors.append("Please insert Your name")
        elif len(postData["name"])<3:
            errors.append("Name needs to be 3-45 characters")
        elif not re.search(r'^[A-Za-z]+$', postData["name"]):
            errors.append("Name needs to be in alphabets")
        if len(postData["username"])==0:
            errors.append("Please insert an username address in the bracket")
        elif len(postData["username"])<3:
            errors.append("Username needs to more greater than 3-45 characters")
        elif len(User.objects.filter(username=postData["username"]))>0:
            errors.append("username is already")
        if len(postData["password"])<8:
            errors.append("Password needs to more than 8 characters")
        if postData["confirm"] != postData["password"]:
            errors.append("Make sure password and confirmation matches!")
        if len(errors)==0:
            user= User.objects.create(name=postData["name"], username= postData["username"], pw_hash= bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt()))
            return(True,user)
        else:
            return(False,errors)

    def authenticate(self, postData):
        if "username"in postData and "password" in postData:
            try:
                # print 80*"*"
                # print 'User.objects.filter(username=postData["username"])', User.objects.get(username=postData["username"])
                user = User.objects.get(username=postData["username"])
                # print "user.pw_hash", user.pw_hash
                # print 80*"*"
            except User.DoesNotExist:
                return (False, "Invalid username /password combination")
        pw_match= bcrypt.hashpw(postData['password'].encode(),user.pw_hash.encode())

        if pw_match == user.pw_hash:
            return(True, user)
        else:
            return (False, "Please enter login Information")

class User(models.Model):
    name= models.CharField(max_length=45)
    username= models.CharField(max_length=45)
    pw_hash= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= UserManager()

class TravelManager(models.Manager):
    def addtravel(self,postData,id):
        errors=[]
        if len(postData["destination"])==0:
            errors.append("Please insert your destination")
        if len(postData["description"])==0:
            errors.append("Please insert an username address in the bracket")
        try:
            startdate = datetime.strptime(postData["start"], '%d/%m/%Y')
            enddate = datetime.strptime(postData["end"], '%d/%m/%Y')
        except ValueError:
            errors.append("Invalid date of birth entered. Use MM/DD/YYYY format.")
        else:
            if datetime.now() > startdate:
                errors.append("Travel Date from cannot be in the past")
            if datetime.now() > enddate:
                errors.append("Travel Date To cannot be in the past")
            elif startdate > enddate:
                errors.append("Travel Date from cannot be future of Travel Date To")
        if len(errors)==0:
            this_user= User.objects.get(id=id)
            addtravel= Travel.objects.create(traveler= this_user, destination= postData["destination"], description= postData["description"], start= postData["start"], end= postData["end"])
            return(True,addtravel)
        else:
            return(False,errors)

class Travel(models.Model):
    traveler= models.ForeignKey(User)
    destination= models.CharField(max_length=255, blank=True, null=True)
    description= models.TextField(max_length=1000)
    start= models.DateTimeField(['%d/%m/%Y'],blank=True, null=True)
    end= models.DateTimeField(['%d/%m/%Y'], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()
