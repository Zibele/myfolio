from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    

class Skill(models.Model):

    title= models.CharField(max_length=250)
    CATEGORY_OPTIONS= (("language","Language"),("framework","Framework"),("tool","Tool"),)
    category= models.CharField(max_length=250,choices=CATEGORY_OPTIONS,default="language")







