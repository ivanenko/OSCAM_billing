from billing.views import PackageListPage, remove_package, create_package, add_package_to_user, PaymentListPage, remove_payment, create_payment
from user_profile.views import HomeRedirectPageView, SuperuserIndexPage, DealerIndexPage, UserProfilePage, CreateUserPage, UserListPage, \
    UserDetailsPage, deactivate_user, activate_user, remove_user, DealerListPage
import os
#import patches
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
from django.views.generic import TemplateView

def get_urls():
    urls = []
    for appname in settings.INSTALLED_APPS:
        if appname.startswith('django.'):
            continue

        dname = os.path.dirname(__import__(appname).__file__)
        if os.path.isfile(os.path.join(dname, "urls.py")):
            urls.append(url(r'^%s/' % appname, include('%s.urls' % appname, namespace=appname, app_name=appname)))

        if os.path.isfile(os.path.join(dname, "absolute_urls.py")):
            urls.append(url('', include('%s.absolute_urls' % appname)))

    return urls


urlpatterns = patterns('',

           url(r'^$', HomeRedirectPageView.as_view(), name='home'),
           url(r'^superuser_index.html$', SuperuserIndexPage.as_view(), name='superuser_index'),
           url(r'^dealer_index.html$', DealerIndexPage.as_view(), name='dealer_index'),
           url(r'^profile.html$', UserProfilePage.as_view(), name='profile'),
           url(r'^create_user.html$', CreateUserPage.as_view(), name='create_user'),
           url(r'^user_list.html$', UserListPage.as_view(), name='user_list'),
           url(r'^dealer_list.html$', DealerListPage.as_view(), name='dealer_list'),
           url(r'^user_details/(?P<pk>\d+)$', UserDetailsPage.as_view(), name='user_details'),

           url(r'^package_list.html$', PackageListPage.as_view(), name='package_list'),
           url(r'^remove_package/(?P<pk>\d+)$', remove_package, name='remove_package'),
           url(r'^create_package.html$', create_package, name='create_package'),
           url(r'^add_package_to_user/(?P<user_id>\d+)$', add_package_to_user, name='add_package_to_user'),

           url(r'^payments.html$', PaymentListPage.as_view(), name='payments'),
           url(r'^remove_payment/(?P<pk>\d+)$', remove_payment, name='remove_payment'),
           url(r'^create_payment.html$', create_payment, name='create_payment'),

           url(r'^deactivate_user/(?P<user_id>\d+)$', deactivate_user, name='deactivate_user'),
           url(r'^activate_user/(?P<user_id>\d+)$', activate_user, name='activate_user'),
           url(r'^remove_user/(?P<user_id>\d+)$', remove_user, name='remove_user'),

           url(r'^accounts/login$', 'django.contrib.auth.views.login', name='login'),
           url(r'^accounts/logout$', 'django.contrib.auth.views.logout', {'next_page' : 'home'}, name='logout'),

           # url(r'^create_user.html', 'myapp.views.create_new_user', name='new_user'),
           #url(r'^login.html', 'myapp.views.login_user', name='login'),
           #url(r'^logout.html', 'myapp.views.logout_user', name='logout'),
           #url(r'^startpage.html', TemplateView.as_view(template_name='wellcome.html'), name='start'),
           #url(r'^create_product.html', CreateProductView.as_view(), name='create_product'),

           #url(r'^admin/', include(admin.site.urls)),
           *get_urls()
)
