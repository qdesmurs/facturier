# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *

from devis import Create_estimate

from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

@login_required
@permission_required('post.add_post')
def create_estimate(request):
    form = Create_estimate()
    if request.method == "POST":
        form = Create_estimate(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
    context = {
        'form' : form
    }
    return render(request, "devis.html", context)
