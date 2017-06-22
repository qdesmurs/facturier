# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# class Customer(models.Model):
#     dealer = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#
# class Status(models.Model):
#     status = models.CharField(max_length=100)
#
# class Proposal(models.Model):
#     dealer = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.ForeignKey(Status, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#
# class Service(models.Model):
#     service_name = models.CharField(max_length=200)
#     unit_price = models.DecimalField(max_digits=8, decimal_places=2)
#     quantity = models.SmallIntegerField()
#     proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)

class Client(models.Model):
    name = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Status(models.Model):
    status_label = models.CharField(max_length=50, blank=True, null=True)

class Project(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=False, auto_now_add=False)

class Project_line(models.Model):
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
