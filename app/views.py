# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

from .models import *

from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic import CreateView, DetailView, ListView

from django.views.generic.edit import UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from .forms import *

import datetime

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

class DevisListView(ListView):
    model = Project
    template_name = "devislist.html"
    def get_context_data(self):
        context = ListView.get_context_data(self)
        context['devEnCours'] = Project.objects.filter(status = "Devis en Cours")
        context['factEnCours'] = Project.objects.filter(status = "Facture en Cours")
        return context

class TresListView(ListView):
    model = Project
    template_name = "tresorerie.html"
    def get_context_data(self):
        context = ListView.get_context_data(self)
        fpayee = Project.objects.filter(status = "Facture Payée")
        context["factpayee"] = fpayee
        total = 0
        for i in fpayee:
            total += i.amount()
        context["total"] = total
        return context

class ArchiveListView(ListView):
    model = Project
    template_name = "archives.html"
    def get_context_data(self):
        context = ListView.get_context_data(self)
        context['devPerdu'] = Project.objects.filter(status = "Devis Perdu")
        context['factPayee'] = Project.objects.filter(status = "Facture Payée")
        return context

class DevisDetails(DetailView):
    model = Project
    slug_field = "name"
    context_object_name = "details"
    template_name = "devisdetails.html"

class CreateClient(CreateView):
    model = Client
    fields = ("name",)
    template_name = "createclient.html"
    success_url = reverse_lazy('devis')

class CreateDevis(CreateView):
    model = Project
    template_name = 'devis.html'
    fields = ("name", "id_user", "id_client", "status", "creation_date",)
    success_url = reverse_lazy('devislist')

    def get_context_data(self, form=None):
        context = CreateView.get_context_data(self)
        context["app_formset"] = LineFormSet()
        return context

    def form_valid(self, form):
        app_resp = CreateView.form_valid(self, form)
        app_formset = LineFormSet(self.request.POST, instance=self.object)

        if app_formset.is_valid():
            app_formset.save()

        return app_resp

    def get_success_url(self):
        return reverse('devislist')

class DevisUpdate(UpdateView):
    model = Project
    slug_field = "name"
    fields = ("status",)
    def get_success_url(self):
       return reverse('devisdetails', kwargs={'slug': self.object.name})

class DevisDelete(DeleteView):
    model = Project
    slug_field = "name"
    success_url = reverse_lazy("devislist")

def change_status(request, name):
   now = datetime.datetime.now()
   prop = Project.objects.get(name=name)
   prop.status = "Facture en Cours"
   prop.date_acceptance = now
   prop.save()
   return redirect("devislist")

def arch_proposal(request, name):
   now = datetime.datetime.now()
   prop = Project.objects.get(name=name)
   if prop.status == "Devis en Cours":
       prop.status = "Devis Perdu"
       prop.date_refusal = now
   else:
       prop.status = "Facture Payée"
       prop.date_payment = now
   prop.save()
   context = {
       "project" : prop
   }
   return redirect('archive')
