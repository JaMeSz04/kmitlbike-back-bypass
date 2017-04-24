from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.status import *


def token_required(view_func):
    @csrf_exempt
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
        if auth_header:
            token = str(auth_header)
            try:
                request.token = Token.objects.get(pk=token)
                request.user = request.token.user
                if not request.token.user.is_active:
                    return HttpResponse(status=HTTP_401_UNAUTHORIZED, content_type="application/json")
            except Token.DoesNotExist:
                return HttpResponse(status=HTTP_401_UNAUTHORIZED, content_type="application/json")
            return view_func(request, *args, **kwargs)
        return HttpResponse(status=HTTP_403_FORBIDDEN, content_type="application/json")
    return _wrapped_view
