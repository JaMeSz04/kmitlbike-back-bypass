from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from kmitl_bike_django import settings
from accounts.api import *
from bikes.api import *
from histories.api import *
from info.api import *
from reports.api import *
from versions.api import *

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/accounts/access_token', api_access_token.as_view()),
    url(r'^api/v1/accounts/login', api_login.as_view()),
    url(r'^api/v1/accounts/logout', api_logout.as_view()),
    url(r'^api/v1/accounts/register', api_register.as_view()),
    url(r'^api/v1/bikes/list', api_get_available_bikes.as_view()),
    url(r'^api/v1/bikes/plans/list', api_get_bike_usage_plans.as_view()),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/borrow', api_borrow_bike.as_view()),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/return', api_return_bike.as_view()),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/update', api_update_bike_location.as_view()),
    url(r'^api/v1/users/(?P<user_id>\d+)/profile', api_profile.as_view()),
    url(r'^api/v1/users/(?P<user_id>\d+)/session', api_get_user_session.as_view()),
    url(r'^api/v1/users/(?P<user_id>\d+)/histories/list', api_get_user_history_list.as_view()),
    url(r'^api/v1/users/(?P<user_id>\d+)/histories/(?P<hist_id>\d+)', api_get_user_history.as_view()),
    url(r'^api/v1/reports/types/list', api_get_report_type.as_view()),
    url(r'^api/v1/reports/send_report', api_send_report.as_view()),
    url(r'^api/v1/reports/send_feedback', api_send_feedback.as_view()),
    url(r'^api/v1/versions/check', api_check_update.as_view()),
    url(r'^api/v1/info/terms_conditions', api_get_terms_conditions.as_view()),
    url(r'^api/v1/info/credits', api_get_credits.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
