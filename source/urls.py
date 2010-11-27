from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
<<<<<<< HEAD
# from django.contrib import admin
# admin.autodiscover()
=======
from django.contrib import admin
admin.autodiscover()
>>>>>>> melveg/master

urlpatterns = patterns('',
    # Example:
    # (r'^source/', include('source.foo.urls')),

<<<<<<< HEAD
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
=======
    # Uncomment the admin/doc line below to enable admin documentation:
>>>>>>> melveg/master
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
=======
    (r'^recordlist/(?P<table_id>\d+)/$', 'recordlist.views.index'),
    (r'^gcomment/(?P<table_id>\d+)/$', 'gcomment.views.index'),
    (r'^gcomment/create/((?P<table_id>\d+)/)*$', 'gcomment.views.create'),
    (r'^comments/', include('django.contrib.comments.urls')),
>>>>>>> melveg/master
)
