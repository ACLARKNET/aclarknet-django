from django.http import HttpResponseRedirect
from django.shortcuts import render
from aclarknet.aclarknet.forms import ContactForm
from aclarknet.aclarknet.models import Client
from aclarknet.aclarknet.models import Service
from aclarknet.aclarknet.models import TeamMember
from aclarknet.aclarknet.models import Testimonial


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def book(request):
    return render(request, 'book.html')


def clients(request):
    clients = Client.objects.order_by('name')
    context = {'clients': clients}
    return render(request, 'clients.html', context)


def community(request):
    return render(request, 'community.html')


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
            recipients = ['info@aclark.net']
            import datetime
            subject = 'ACLARK.NET Contact Form Submission %s' % datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
            send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/contact/thanks')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def history(request):
    return render(request, 'history.html')


def home(request):
    testimonials = Testimonial.objects.order_by('?')
    testimonial = None
    if len(testimonials) > 0:
        testimonial = testimonials[0]
    context = {'testimonial': testimonial}
    return render(request, 'home.html', context)


def location(request):
    return render(request, 'location.html')


def open_source(request):
    return render(request, 'open_source.html')


def technologies(request):
    return render(request, 'technologies.html')


def services(request):
    services = Service.objects.order_by('name')
    context = {'services': services}
    return render(request, 'services.html', context)


def team(request):
    members = TeamMember.objects.order_by('name')
    context = {'members': members}
    return render(request, 'team.html', context)


def testimonials(request):
    testimonials = Testimonial.objects.order_by('-date')
    context = {'testimonials': testimonials}
    return render(request, 'testimonials.html', context)


def thanks(request):
    return render(request, 'thanks.html')


