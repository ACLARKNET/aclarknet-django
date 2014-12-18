from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.client_name


class Service(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name
