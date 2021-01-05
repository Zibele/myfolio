from django.shortcuts import render
from .models import Profile, ProfileSkill, Project, TechStack,Skill



def index_page(request):

    profile = Profile.objects.get(name='Zibele')
    projects = Project.objects.filter(profile_id=profile)
    techStack = TechStack.objects.all()
    skills = ProfileSkill.objects.filter(profile_id=profile)

    return render(request,'myfolio/my_folio_app/templates/myfolio/my_folio_app/index.html',
    {'profile' : Profile, })