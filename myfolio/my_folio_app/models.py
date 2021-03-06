from django.db import models
from django.shortcuts import get_object_or_404

class Profile(models.Model):

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name + ' ' + self.surname
    
    class meta:
        db_table='"Profiles"'

class Project(models.Model):

    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    project_title = models.CharField(max_length=30)
    project_svg = models.TextField(null=True)
    logo_svg = models.TextField(null=True) 
    description = models.TextField()
    
    def __str__(self):
        return self.project_title
    
    class meta:
        db_table='"Projects"'

class Category(models.Model):

    category_name= models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name 
    
    class meta:
        db_table='"Categories"'



class Skill(models.Model):

    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name= models.CharField(max_length=30)
    skill_svg_large= models.TextField(null = True)
    skill_svg_small= models.TextField(null = True)
    display_svg= models.BooleanField(default = True)
    display_name = models.BooleanField(default = True)
    
    def __str__(self):
        return self.skill_name

    class meta:
        db_table='"Skills"'

class ProfileSkill(models.Model):

    profile= models.ForeignKey(Profile,on_delete = models.CASCADE)
    skill=models.ForeignKey(Skill,on_delete= models.CASCADE)

    class meta:
        db_table='"ProfileSkills"'

class TechStack(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class meta:
        db_table='"TechStack"'
