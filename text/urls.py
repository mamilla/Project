from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'text.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^home/$', 'Customer.views.home', name='home'),
    url(r'^upload/$', 'Customer.views.upload_file', name='upload'),
    # url(r'^customerdetail/$', 'Customer.views.customerdetail', name='customerdetail'),
    url(r'^transactiondetail/$', 'Customer.views.transactiondetail', name='transactiondetail'),
    

    url(r'^admin/', include(admin.site.urls)),
]
