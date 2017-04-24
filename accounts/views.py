import json

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.status import *

from accounts.backends import KMITLBackend
from accounts.forms import UserValidationForm
from accounts.models import UserProfile
from kmitl_bike_django.decorators import token_required


class AuthenticationAPI(object):

    @staticmethod
    def access_token(request):
        if request.method == "POST":
            token = request.POST.get("token")
            try:
                token, _ = Token.objects.get_or_create(key=token)
                response = {"token": token.key}
                return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
            except IntegrityError:
                return HttpResponse(status=HTTP_401_UNAUTHORIZED, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    def login(request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            result, token = KMITLBackend.authenticate(username, password)
            if result == "exists":
                if token:
                    user = token.user
                    if user.is_active:
                        response = {"result": "exists",
                                    "token": str(token),
                                    "first_name": user.first_name,
                                    "last_name": user.last_name,
                                    "gender": user.gender,
                                    "email": user.email,
                                    "phone_no": user.phone_no}
                        return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
                    else:
                        response = {"result": "banned"}
                        return HttpResponse(json.dumps(response), status=HTTP_401_UNAUTHORIZED, content_type="application/json")
            elif result == "first_time":
                response = {"result": "first_time"}
                return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
            response = {"result": "denied"}
            return HttpResponse(json.dumps(response), status=HTTP_401_UNAUTHORIZED, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    @token_required
    def logout(request):
        if request.method == "GET":
            request.token.delete()
            return HttpResponse(status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    def register(request):
        if request.method == "POST":
            try:
                user_form = UserValidationForm(request.POST).get_cleaned_data()
                username = user_form["username"]
                first_name = user_form["first_name"]
                last_name = user_form["last_name"]
                email = user_form["email"]
                gender = user_form["gender"]
                phone_no = user_form["phone_no"]

                try:
                    user = User.objects.create_user(username=username,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    email=email)
                    UserProfile.objects.create(user=user, gender=gender, phone_no=phone_no)
                    try:
                        User.objects.get(username=username)
                        return HttpResponse(status=HTTP_201_CREATED, content_type="application/json")
                    except User.DoesNotExist:
                        response = {"message": "Fail to create new user. Please try again later."}
                        return HttpResponse(json.dumps(response), status=HTTP_406_NOT_ACCEPTABLE,
                                            content_type="application/json")
                except IntegrityError:
                    response = {"message": "This user already exists"}
                    return HttpResponse(json.dumps(response), status=HTTP_406_NOT_ACCEPTABLE,
                                        content_type="application/json")
            except ValidationError as e:
                response = {"message": str(e.message)}
                return HttpResponse(json.dumps(response), status=HTTP_406_NOT_ACCEPTABLE, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")


class AccountsAPI(object):

    @staticmethod
    @token_required
    def get_user_session(request, user_id=None):
        if request.method == "GET":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    @token_required
    def get_user_history_list(request, user_id=None):
        if request.method == "GET":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")

    @staticmethod
    @token_required
    def get_user_history(request, user_id=None, hist_id=None):
        if request.method == "GET":
            return HttpResponse(json.dumps(response), status=HTTP_200_OK, content_type="application/json")
        else:
            return HttpResponse(status=HTTP_405_METHOD_NOT_ALLOWED, content_type="application/json")
