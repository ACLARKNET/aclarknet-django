from django.shortcuts import render
from aclarknet.aclarknet.models import Service
from aclarknet.aclarknet.models import TeamMember


def home(request):
    return render(request, 'home.html')


def projects(request):
    return render(request, 'projects.html')


def services(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'services.html', context)


def team(request):
    members = TeamMember.objects.all()
    context = {'members': members}
    return render(request, 'team.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
