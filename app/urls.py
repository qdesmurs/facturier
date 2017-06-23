from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', homepage, name="homepage"),
    url(r'^create', CreateDevis.as_view(), name='devis')
]
