from django.db import models


class Client(models.Model):
    name = models.CharField(default=None, max_length=60)
    text = models.TextField(default=None)

    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=60)
    icon = models.CharField(default=None, max_length=30)
    text = models.TextField(default=None)

    def __unicode__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=60)
    desc = models.CharField(default=None, max_length=60)
    icon = models.CharField(default=None, max_length=30)
    text = models.TextField(default=None)

    def __unicode__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=90, default=None)
    text = models.TextField()

    def __unicode__(self):
        return self.name
