from django.shortcuts import render
from .models import Profile, ProfileSkill, Project, TechStack,Skill



def index_page(request):

    profile = Profile.objects.get(name='Zibele')
    projects = Project.objects.filter(profile=profile)
    tech_stacks = TechStack.objects.all()
    profile_skills = ProfileSkill.objects.select_related('skill','skill__category').filter(profile=profile)
    return render(request,'my_folio_app/index.html',{'profile' : profile,
    'projects': projects,'techStacks': tech_stacks,'profile_skills':profile_skills})