from django.http import HttpResponse
from rest_framework.status import *

from versions.utils import requires_update, get_latest_version


def check_update(request):
    if request.method == 'POST':
        platform = request.POST.get("platform")
        app_version = request.POST.get("app_version")
        b_requires_update, update_url = requires_update(platform, app_version)
        if b_requires_update:
            response = {'requires_update': True,
                        'update_url': update_url,
                        'platform': platform,
                        'critical_version': get_latest_version(platform)}
        else:
            response = {'requires_update': False}
        return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
    else:
        return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")