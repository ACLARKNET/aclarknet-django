from django.http import HttpResponseRedirect
from django.shortcuts import render
from aclarknet.aclarknet.forms import ContactForm
from aclarknet.aclarknet.models import Client
from aclarknet.aclarknet.models import Service
from aclarknet.aclarknet.models import TeamMember
from aclarknet.aclarknet.models import Testimonial


def book(request):
    return render(request, 'book.html')


def clients(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clients.html', context)


def home(request):
    testimonials = Testimonial.objects.order_by('?')
    testimonial = None
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
    testimonials = Testimonial.objects.order_by('-date')
    context = {'testimonials': testimonials}
    return render(request, 'testimonials.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    # https://docs.djangoproject.com/en/1.7/topics/forms/#the-view
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            from django.core.mail import send_mail
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = ['aclark@aclark.net']
            subject = 'Test'
            send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/contact/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
