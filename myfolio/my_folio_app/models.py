from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    jobTitle = models.CharField(max_length=30)
    
class Project(models.Model):

    profileId = models.ForeignKey(Profile,)
    projectTitle = models.CharField(max_length=30)
    description = models.TextField()

class Skill(models.Model):



class TechStack(models.Model):







class Skill(models.Model):

    title= models.CharField(max_length=250)
    CATEGORY_OPTIONS= (("language","Language"),("framework","Framework"),("tool","Tool"),)
    category= models.CharField(max_length=250,choices=CATEGORY_OPTIONS,default="language")







