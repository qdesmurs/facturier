# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

from .models import *

from django.forms import inlineformset_factory

from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic import CreateView

from .forms import *


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

class CreateDevis(CreateView):
    model = Project
    template_name = 'devis.html'
    fields = "__all__"

    def lines(self):
        if self.request.POST:
            return lineFormSet(self.request.POST)
        else :
            return lineFormSet()

    def form_valid(self, form):
        product = self.lines()
        self.object = form.save()
        if product.is_valid():
            product.instance = self.object
            product.save()
        return super(CreateDevis, self).form_valid(form)

    def get_success_url(self):
        return reverse('homepage')

#
# @login_required
# @permission_required('post.add_post')
# def create_estimate(request):
#     lineFormSet = inlineformset_factory(Project, Project_line, fields=['label', 'quantity', 'unit_price'] , extra=1)
#     form = lineFormSet()
#     if request.method == "POST":
#         form = lineFormSet(request.POST)
#         if form.is_valid():
#             post = form.save()
#
#             context = {
#             'form' : form
#             }
#             return render(request, "devis.html", context)
