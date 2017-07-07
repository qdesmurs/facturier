from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', homepage, name="homepage"),
    url(r'^createclient', CreateClient.as_view(), name='createclient'),
    url(r'^create', CreateDevis.as_view(), name='devis'),
    url(r'^list', DevisListView.as_view(), name='devislist'),
    url(r'^tresorerie', TresListView.as_view(), name='tresorerie'),
    url(r'^archive', ArchiveListView.as_view(), name='archive'),
    url(r'^(?P<slug>[\w-]+)/$', DevisDetails.as_view(), name='devisdetails'),
    url(r'^(?P<slug>[\w-]+)/edit/$', DevisUpdate.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', DevisDelete.as_view(), name='delete'),
    url(r'^(?P<name>[\w-]+)/change$', change_status, name="project-change"),
    url(r'^(?P<name>[\w-]+)/arch$', arch_proposal, name="project-arch"),
]
