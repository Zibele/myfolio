from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    jobTitle = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name + ' ' + self.surname
    
    class meta:
        db_table='"Profiles"'

class Project(models.Model):

    profileId = models.ForeignKey(Profile,on_delete=models.CASCADE)
    projectTitle = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.projectTitle
    
    class meta:
        db_table='"Projects"'

class Category(models.Model):

    categoryName= models.CharField(max_length=30)
    
    def __str__(self):
        return self.categoryName 
    
    class meta:
        db_table='"Categories"'

class Skill(models.Model):

    categoryId=models.ForeignKey(Category, on_delete=models.CASCADE)
    skillName= models.CharField(max_length=30)
    
    def __str__(self):
        return self.skillName

    class meta:
        db_table='"Skills"'

class TechStack(models.Model):

    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    skillId = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class meta:
        db_table='"TechStack"'









