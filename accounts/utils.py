from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from accounts.models import UserProfile


class UserValidationForm(object):

    def __init__(self, request):
        self.cleaned_data = {}
        self.username = request.get("username", None)
        self.first_name = request.get("first_name", None)
        self.last_name = request.get("last_name", None)
        self.email = request.get("email", None)
        self.gender = request.get("gender", None)
        self.phone_no = request.get("phone_no", None)

    def clean(self):
        self.cleaned_data["username"] = self.clean_username()
        self.cleaned_data["first_name"] = self.clean_first_name()
        self.cleaned_data["last_name"] = self.clean_last_name()
        self.cleaned_data["email"] = self.clean_email()
        self.cleaned_data["gender"] = self.clean_gender()
        self.cleaned_data["phone_no"] = self.clean_phone_no()

    def clean_username(self):
        if self.username is None or " " in self.username or len(self.username) < 8:
            raise ValidationError("Please enter a valid username.")
        return self.username.lower().strip()

    def clean_first_name(self):
        if self.first_name is None or len(self.first_name) < 1:
            raise ValidationError("Please enter a valid first name.")
        return self.first_name.strip()

    def clean_last_name(self):
        if self.last_name is None or len(self.last_name) < 1:
            raise ValidationError("Please enter a valid last name.")
        return self.last_name.strip()

    def clean_email(self):
        validate_email(self.email)
        return self.email.strip()

    def clean_gender(self):
        if self.gender is None:
            raise ValidationError("Please select a valid gender.")
        try:
            if int(self.gender) not in [UserProfile.Gender.MALE, UserProfile.Gender.FEMALE, UserProfile.Gender.OTHER]:
                return UserProfile.Gender.OTHER
            return int(self.gender)
        except ValueError:
            raise ValidationError("Gender must be integer.")

    def clean_phone_no(self):
        if self.phone_no is None or len(self.phone_no) < 10:
            raise ValidationError("Please enter a valid phone number.")
        return self.phone_no.strip()

    def get_cleaned_data(self):
        if not self.cleaned_data:
            self.clean()
        return self.cleaned_data

