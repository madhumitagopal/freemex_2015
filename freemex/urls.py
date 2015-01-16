from django.conf.urls import patterns, include, url
from freemex.login import init,call_to_register,register
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #(r'^now/check_template/$',current_datetime),
    (r'^freemex/login/$',init),
    (r'^freemex/register/$',call_to_register),
    # Examples:
    # url(r'^$', 'freemex.views.home', name='home'),
    # url(r'^freemex/', include('freemex.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
