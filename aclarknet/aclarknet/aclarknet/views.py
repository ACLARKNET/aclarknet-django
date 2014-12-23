from django.shortcuts import render
from aclarknet.aclarknet.models import Client
from aclarknet.aclarknet.models import Service
from aclarknet.aclarknet.models import TeamMember
from aclarknet.aclarknet.models import Testimonial


def clients(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clients.html', context)


def home(request):
    testimonials = Testimonial.objects.order_by('?')
    if len(testimonials) > 0:
        testimonial = testimonials[0]
    context = {'testimonial': testimonial}
    return render(request, 'home.html', context)


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


def testimonials(request):
    testimonials = Testimonial.objects.all()
    context = {'testimonials': testimonials}
    return render(request, 'testimonials.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
