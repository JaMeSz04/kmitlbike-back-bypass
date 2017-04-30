from django.conf.urls import url, include
from django.contrib import admin

from accounts.api import api_access_token, api_login, api_logout, api_register, api_profile
from bikes.api import api_get_available_bikes, api_borrow_bike

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/accounts/access_token', api_access_token.AccessTokenView.as_view()),
    url(r'^api/v1/accounts/login', api_login.LoginView.as_view()),
    url(r'^api/v1/accounts/logout', api_logout.LogoutView.as_view()),
    url(r'^api/v1/accounts/register', api_register.RegisterView.as_view()),
    url(r'^api/v1/accounts/profile', api_profile.ProfileView.as_view()),
    # url(r'^api/v1/histories/(?P<user_id>\d+)/session', get_user_session),
    # url(r'^api/v1/histories/(?P<user_id>\d+)/history/list', get_user_history_list),
    # url(r'^api/v1/histories/(?P<user_id>\d+)/history/(?P<hist_id>\d+)', get_user_history),
    url(r'^api/v1/bikes/list', api_get_available_bikes.GetAvailableBikesView.as_view()),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/borrow', api_borrow_bike.BorrowBikeView.as_view()),
    # url(r'^api/v1/bikes/(?P<bike_id>\d+)/return', return_bike),
    # url(r'^api/v1/bikes/(?P<bike_id>\d+)/update', update_bike_location),
    # url(r'^api/v1/reports/send_report', send_report),
    # url(r'^api/v1/reports/send_feedback', send_feedback),
    # url(r'^api/v1/versions/check_update', check_update),
    # url(r'^api/v1/versions/terms_conditions', get_terms_conditions),
]
