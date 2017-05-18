# coding=utf-8
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token

from accounts.models import UserExtraProfile


class KMITLBackend(object):

    class Information(object):
        KMITL_ID = 3
        FIRST_NAME = 6
        LAST_NAME = 9
        ID_CARD = 12
        PHONE_NO = 15
        FACULTY = 18
        FORWARD_EMAIL = 22
        EMAIL = 24

    class Status(object):
        FIRST_TIME = 1
        ALREADY_EXISTS = 2
        INVALID = 3
        CONNECTION_FAIL = 4

    NAC_KMITL_URL = "https://nac.kmitl.ac.th/dana-na/auth/url_default/login.cgi"

    IAM_KMITL_URL = "https://iam.kmitl.ac.th/statusProfile.php"

    @staticmethod
    def authenticate(username=None, password=None):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        form_data = {
            "tz_offset": 420,
            "username": username.lower().strip(),
            "password": password,
            "realm": "ระบบแอคเคาท์ใหม่ (Generation2)",
            "btnSubmit": "Sign In"}
        try:
            requests.post(KMITLBackend.NAC_KMITL_URL, form_data, headers=headers, verify=False, allow_redirects=False)
            response = requests.post(KMITLBackend.NAC_KMITL_URL, form_data, headers=headers, verify=False, allow_redirects=False)
            if response.status_code == 302:
                if KMITLBackend.is_authenticated(response):
                    user = KMITLBackend.get_user(username)
                    if user:
                        KMITLBackend.get_user_information(username, password, user)
                        token, _ = Token.objects.get_or_create(user=user)
                        return KMITLBackend.Status.ALREADY_EXISTS, token
                    else:
                        return KMITLBackend.Status.FIRST_TIME, None
                else:
                    return KMITLBackend.Status.INVALID, None
            else:
                return KMITLBackend.Status.CONNECTION_FAIL, None
        except requests.HTTPError:
            return KMITLBackend.Status.CONNECTION_FAIL, None

    @staticmethod
    def is_authenticated(responses):
        location = responses.headers.get("location")
        result_check = KMITLBackend.read_url_params(location, "check")
        result_p = KMITLBackend.read_url_params(location, "p")
        if result_check == "yes" or result_p == "session-limit":
            return True
        else:
            return False

    @staticmethod
    def get_user(username=None):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user_type(username=None):
        # TODO: check user type
        # return "staff"
        return "student"

    @staticmethod
    def get_user_information(username=None, password=None, user=None):
        if not UserExtraProfile.objects.filter(user=user).exists():
            username = username.replace("@kmitl.ac.th", "")
            headers = {
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://iam.kmitl.ac.th",
                "Referer": "https://iam.kmitl.ac.th/signAgreement.php",
                "Accept-Language": "en-US,en;q=0.8,th;q=0.6"}
            form_data = {
                "manage_login": username.lower().strip(),
                "manage_pass": password,
                "PeopleType": KMITLBackend.get_user_type(username),
                "accept": "+ยอมรับ+(Accept)+"}
            try:
                response = requests.post(KMITLBackend.IAM_KMITL_URL,
                                         form_data,
                                         headers=headers,
                                         verify=False,
                                         allow_redirects=False)

                if response.status_code == 200:
                    response.encoding = "utf-8"
                    soup = BeautifulSoup(response.text, "html.parser")
                    information = soup.section.find_all("font")
                    kmitl_id = information[KMITLBackend.Information.KMITL_ID].string
                    first_name = information[KMITLBackend.Information.FIRST_NAME].string
                    last_name = information[KMITLBackend.Information.LAST_NAME].string
                    id_card = information[KMITLBackend.Information.ID_CARD].string
                    phone_no = information[KMITLBackend.Information.PHONE_NO].string
                    faculty = information[KMITLBackend.Information.FACULTY].string
                    email = information[KMITLBackend.Information.EMAIL].string
                    forward_email = information[KMITLBackend.Information.FORWARD_EMAIL].string

                    try:
                        UserExtraProfile.objects.create(user=user,
                                                        kmitl_id=kmitl_id,
                                                        first_name=first_name,
                                                        last_name=last_name,
                                                        id_card=id_card,
                                                        phone_no=phone_no,
                                                        faculty=faculty,
                                                        email=email,
                                                        forward_email=forward_email)
                    except IntegrityError:
                        pass
            except requests.HTTPError:
                pass

    @staticmethod
    def read_url_params(url, parameter):
        param = url[url.index("?") + 1:]
        data_lst = param.split("&")
        for data in data_lst:
            if data[:data.index("=")] == parameter:
                return data[data.index("=") + 1:]
        return None
