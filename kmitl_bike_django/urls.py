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
from django.conf.urls import url
from django.contrib import admin

from accounts.views import AuthenticationAPI, AccountsAPI
from bikes.views import BikesAPI
from reports.views import ReportsAPI
from services.views import StatusAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/access_token', AuthenticationAPI.access_token),
    url(r'^api/v1/auth/login', AuthenticationAPI.login),
    url(r'^api/v1/auth/logout', AuthenticationAPI.logout),
    url(r'^api/v1/auth/register', AuthenticationAPI.register),
    url(r'^api/v1/accounts/(?P<user_id>\d+)/session', AccountsAPI.get_user_session),
    url(r'^api/v1/accounts/(?P<user_id>\d+)/history/list', AccountsAPI.get_user_history_list),
    url(r'^api/v1/accounts/(?P<user_id>\d+)/history/(?P<hist_id>\d+)', AccountsAPI.get_user_history),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/list', BikesAPI.get_available_bikes),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/borrow', BikesAPI.borrow_bike),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/return', BikesAPI.return_bike),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/update', BikesAPI.update_bike_location),
    url(r'^api/v1/reports/send_report', ReportsAPI.send_report),
    url(r'^api/v1/reports/send_feedback', ReportsAPI.send_feedback),
    url(r'^api/v1/services/check_update', StatusAPI.check_update),
    url(r'^api/v1/services/terms_conditions', StatusAPI.get_terms_conditions),
]
