from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', homepage),
    url(r'^create', create_estimate, name='devis')
]
