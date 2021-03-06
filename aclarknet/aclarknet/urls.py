from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'aclarknet.aclarknet.views.home', name='home'),
    url(r'^about/blog', 'aclarknet.aclarknet.views.blog', name='blog'),
    url(r'^about/book', 'aclarknet.aclarknet.views.book', name='book'),
    url(r'^about/clients', 'aclarknet.aclarknet.views.clients', name='clients'),
    url(r'^about/community', 'aclarknet.aclarknet.views.community', name='community'),
    url(r'^about/history', 'aclarknet.aclarknet.views.history', name='history'),
    url(r'^about/location', 'aclarknet.aclarknet.views.location', name='location'),
    url(r'^about/open-source', 'aclarknet.aclarknet.views.open_source', name='open_source'),
    url(r'^about/team', 'aclarknet.aclarknet.views.team', name='team'),
    url(r'^about/testimonials', 'aclarknet.aclarknet.views.testimonials', name='testimonials'),
    url(r'^about', 'aclarknet.aclarknet.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/thanks', 'aclarknet.aclarknet.views.thanks', name='thanks'),
    url(r'^contact', 'aclarknet.aclarknet.views.contact', name='contact'),
    url(r'^services', 'aclarknet.aclarknet.views.services', name='services'),
    url(r'^technologies', 'aclarknet.aclarknet.views.technologies', name='technologies'),
)
