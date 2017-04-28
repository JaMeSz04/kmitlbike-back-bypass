from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import *


def token_required(view_func):
    @csrf_exempt
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.META.get('HTTP_AUTHORIZATION', None)
        if auth_header:
            token = str(auth_header)
            try:
                request.token = Token.objects.get(pk=token)
                if request.user is None:
                    request.token.user.update_last_login()
                request.user = request.token.user
                if not request.token.user.is_active:
                    error_message = "This account has been suspended. Please contact our staff for more detail."
                    return Response({"message": error_message}, status=HTTP_401_UNAUTHORIZED)
            except Token.DoesNotExist:
                error_message = "The token is already expired."
                return Response({"message": error_message}, status=HTTP_401_UNAUTHORIZED)
            return view_func(request, *args, **kwargs)
        error_message = "Unauthorized access: No user session provided."
        return Response({"message": error_message}, status=HTTP_401_UNAUTHORIZED)
    return _wrapped_view
