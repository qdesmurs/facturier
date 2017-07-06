# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.
class ProjectInline(admin.TabularInline):
    model = Project_line

class AppAdmin(admin.ModelAdmin):
    inlines = [
        ProjectInline,
]

admin.site.register(Project, AppAdmin)
admin.site.register(Project_line)
admin.site.register(Client)
admin.site.register(Status)
