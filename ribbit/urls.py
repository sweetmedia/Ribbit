from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ribbit.views.home', name='home'),
    # url(r'^ribbit/', include('ribbit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ribbit_app.views.index'), # root
    url(r'^login$', 'ribbit_app.views.login_view'), # login
    url(r'^logout$', 'ribbit_app.views.logout_view'), # logout
    url(r'^signup$', 'ribbit_app.views.signup'), # signup
    url(r'^submit$', 'ribbit_app.views.submit'), #Submit new ribbits
)
