from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from danjaysci import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'danjaysci.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # enable admin
    url(r'^admin/', include(admin.site.urls)),

    # admin documentation
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # my applications
    url(r'^$', 'danjaysci.views.home', name='home'), # home
    url(r'^primers/', include('primers.urls', namespace='primers')), # primers
    url(r'^lab_members/', include('lab_members.urls', namespace='lab_members')), #lab_members

)
