from django.shortcuts import render

# Create your views here.

def check_update(request):
    if request.method == 'POST':
        response = {}

        platform = request.POST.get("platform")
        app_version = request.POST.get("app_version")

        b_requires_update, update_url = AppValidation.requires_update(platform, app_version)

        if b_requires_update:
            response['requires_update'] = True
            response['update_url'] = update_url
            response['platform'] = platform
            response['critical_version'] = AppValidation.get_critical_version(platform)
        else:
            response['requires_update'] = False

        return HttpResponse(json.dumps(response), status=HTTP_200_OK)
    else:
        return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED)

