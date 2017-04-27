from django.http import HttpResponse
from django.template import loader
from rest_framework.status import *


def get_terms_conditions(request):
    if request.method == 'GET':
        template = loader.get_template('terms_conditions.html')
        return HttpResponse(template.render(request), status=HTTP_200_OK)
    else:
        return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")
