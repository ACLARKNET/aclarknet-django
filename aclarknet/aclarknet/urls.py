from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'aclarknet.aclarknet.views.home', name='home'),
    url(r'^projects', 'aclarknet.aclarknet.views.projects', name='projects'),
    url(r'^services', 'aclarknet.aclarknet.views.services', name='services'),
    url(r'^about/clients', 'aclarknet.aclarknet.views.clients', name='clients'),
    url(r'^about/team', 'aclarknet.aclarknet.views.team', name='team'),
    url(r'^about/testimonials', 'aclarknet.aclarknet.views.testimonials', name='testimonials'),
    url(r'^about', 'aclarknet.aclarknet.views.about', name='about'),
    #url(r'^contact', 'aclarknet.aclarknet.views.contact', name='contact'),
    url(r'^contact/', include('contact_form.urls')),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
