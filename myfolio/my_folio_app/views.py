from django.shortcuts import render
from .models import Profile, ProfileSkill, Project, TechStack,Skill



def index_page(request):

    profile = Profile.objects.get(name='Zibele')
    projects = Project.objects.filter(profile_id=profile)
    tech_stacks = TechStack.objects.all()
    skills = ProfileSkill.objects.filter(profile_id=profile)

    return render(request,'my_folio_app/index.html',{'profile' : profile,
    'projects': projects,'techStacks': tech_stacks,'skills':skills})