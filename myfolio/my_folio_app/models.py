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

    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    project_title = models.CharField(max_length=30)
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

    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name= models.CharField(max_length=30)
    
    def __str__(self):
        return self.skill_name

    class meta:
        db_table='"Skills"'

class ProfileSkill(models.Model):

    profile_id = models.ForeignKey(Profile,on_delete = models.CASCADE)
    skill_id=models.ForeignKey(Skill,on_delete= models.CASCADE)

    class meta:
        db_table='"ProfileSkills"'

class TechStack(models.Model):

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class meta:
        db_table='"TechStack"'









