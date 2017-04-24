import json

from django.http import HttpResponse
from django.template import loader
from packaging.version import Version, InvalidVersion
from rest_framework.status import *

from services.models import AppVersion


class StatusAPI(object):

    @staticmethod
    def check_update(request):
        if request.method == 'POST':
            platform = request.POST.get("platform")
            app_version = request.POST.get("app_version")
            b_requires_update, update_url = StatusAPI.requires_update(platform, app_version)
            if b_requires_update:
                response = {'requires_update': True,
                            'update_url': update_url,
                            'platform': platform,
                            'critical_version': StatusAPI.get_latest_version(platform)}
            else:
                response = {'requires_update': False}
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    def requires_update(platform, current_version):
        current_version = Version(current_version)
        try:
            latest_version = StatusAPI.get_latest_version(platform)
            latest_version = Version(latest_version)

            if platform == AppVersion.Platform.ANDROID:
                url = "https://play.google.com/store/apps/details?id=com.bike.kmitl.kmitlbike"
            elif platform == AppVersion.Platform.IOS:
                url = "https://itunes.apple.com/th/app/kmitl-bike/id1133585302"
            else:
                url = "https://www.google.com/search?q=platform+not+supported"
            if current_version < latest_version:
                return True, url
            else:
                return False, None
        except InvalidVersion:
            return False, None

    @staticmethod
    def get_latest_version(platform):
        try:
            app_version = AppVersion.objects.filter(platform=platform).last()
            return app_version.version_code
        except AppVersion.DoesNotExist:
            return None

    @staticmethod
    def get_terms_conditions(request):
        if request.method == 'GET':
            template = loader.get_template('terms_conditions.html')
            return HttpResponse(template.render(request), status=HTTP_200_OK)
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

