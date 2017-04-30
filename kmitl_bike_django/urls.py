from django.conf.urls import url, include
from django.contrib import admin

from accounts.api import api_access_token, api_login, api_logout, api_register, api_profile
from bikes.api import api_get_available_bikes, api_borrow_bike, api_return_bike, api_update_bike_location
from histories.api import api_get_user_session, api_get_user_history_list, api_get_user_history
from reports.api import api_send_report, api_send_feedback
from versions.api import api_check_update
from info.api import api_get_terms_conditions, api_get_credits

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/accounts/access_token', api_access_token.AccessTokenView.as_view()),
    url(r'^api/v1/accounts/login', api_login.LoginView.as_view()),
    url(r'^api/v1/accounts/logout', api_logout.LogoutView.as_view()),
    url(r'^api/v1/accounts/register', api_register.RegisterView.as_view()),
    url(r'^api/v1/bikes/list', api_get_available_bikes.GetAvailableBikesView.as_view()),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/borrow', api_borrow_bike.BorrowBikeView.as_view()),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/return', api_return_bike.ReturnBikeView.as_view()),
    url(r'^api/v1/bikes/(?P<bike_id>\d+)/update', api_update_bike_location.UpdateBikeLocationView.as_view()),
    url(r'^api/v1/users/(?P<user_id>\d+)/profile', api_profile.ProfileView.as_view()),
    url(r'^api/v1/users/(?P<user_id>\d+)/session', api_get_user_session.GetUserSessionView.as_view()),
    url(r'^api/v1/users/(?P<user_id>\d+)/histories/list', api_get_user_history_list.GetUserHistoryListView.as_view()),
    url(r'^api/v1/users/(?P<user_id>\d+)/histories/(?P<hist_id>\d+)', api_get_user_history.GetUserHistoryView.as_view()),
    # url(r'^api/v1/reports/type', send_report),
    url(r'^api/v1/reports/send_report', api_send_report.SendReportView.as_view()),
    url(r'^api/v1/reports/send_feedback', api_send_feedback.SendFeedbackView.as_view()),
    url(r'^api/v1/versions/check', api_check_update.CheckUpdateView.as_view()),
    url(r'^api/v1/info/terms_conditions', api_get_terms_conditions.GetTermsConditionsView.as_view()),
    url(r'^api/v1/info/credits', api_get_credits.GetCreditsView.as_view()),
]
