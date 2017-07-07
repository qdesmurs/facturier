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

STATUS_CHOICES = (
   ("Devis en Cours", 'Devis en cours'),
   ("Facture en Cours", 'Facture en cours'),
   ("Devis Perdu", 'Perdu'),
   ("Facture Payée", 'Payé'),
)

class Client(models.Model):
    name = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __unicode__(self):
        return self.name

class Status(models.Model):
    status_label = models.CharField(max_length=50, blank=True, null=True)
    def __unicode__(self):
        return self.status_label

class Project(models.Model):
    name = models.CharField(max_length=50)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # id_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES)
    creation_date = models.DateField(auto_now_add=False)
    date_refusal = models.DateTimeField(null=True, blank=True)
    date_acceptance = models.DateTimeField(null=True, blank=True)
    date_payment = models.DateTimeField(null=True, blank=True)
    def unit_price(self):
        b = ''
        for j in self.project_line_set.all():
            b = j.unit_price
        return b

    def amount(self):
        result = 0
        for line in self.project_line_set.all():
            result += line.quantity * line.unit_price

        return result

    def quantity(self):
        a = ''
        for i in self.project_line_set.all():
            a = i.quantity
        return a

    def __unicode__(self):
        return self.name

class Project_line(models.Model):
    name = models.CharField(max_length=50)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    def __unicode__(self):
        return self.name
