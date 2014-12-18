from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=60)


class Service(models.Model):
    name = models.CharField(max_length=60)


class TeamMember(models.Model):
    name = models.CharField(max_length=60)
