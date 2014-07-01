from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ims_lti_py_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^/lti/', include('ims_lti_py_sample.urls')),
## LTI urls
    url(r'^lti/', include('ims_lti_py_sample.urls')),

)
