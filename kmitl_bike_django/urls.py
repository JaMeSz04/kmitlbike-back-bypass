"""kmitl_bike_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from accounts.api import api_access_token, api_login, api_logout, api_register


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/accounts/access_token', api_access_token.access_token),
    url(r'^api/v1/accounts/login', api_login.login),
    url(r'^api/v1/accounts/logout', api_logout.logout),
    url(r'^api/v1/accounts/register', api_register.register),
    # url(r'^api/v1/histories/(?P<user_id>\d+)/session', get_user_session),
    # url(r'^api/v1/histories/(?P<user_id>\d+)/history/list', get_user_history_list),
    # url(r'^api/v1/histories/(?P<user_id>\d+)/history/(?P<hist_id>\d+)', get_user_history),
    # url(r'^api/v1/bikes/(?P<bike_id>\d+)/list', get_available_bikes),
    # url(r'^api/v1/bikes/(?P<bike_id>\d+)/borrow', borrow_bike),
    # url(r'^api/v1/bikes/(?P<bike_id>\d+)/return', return_bike),
    # url(r'^api/v1/bikes/(?P<bike_id>\d+)/update', update_bike_location),
    # url(r'^api/v1/reports/send_report', send_report),
    # url(r'^api/v1/reports/send_feedback', send_feedback),
    # url(r'^api/v1/versions/check_update', check_update),
    # url(r'^api/v1/versions/terms_conditions', get_terms_conditions),
]
