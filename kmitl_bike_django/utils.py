from django.db import models
from rest_framework.generics import GenericAPIView
from reversion.admin import VersionAdmin


class AbstractModel(models.Model):

    class Meta:
        abstract = True

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class AbstractAdmin(VersionAdmin):

    list_per_page = 50

    readonly_fields = ("created_date", "updated_date")

    exclude = ("created_date", "updated_date")


class AbstractAPIView(GenericAPIView):

    def get_error_message(self, errors):
        if "non_field_errors" in errors:
            return errors.get("non_field_errors")[0]
        error_message = ""
        for key in errors:
            error_message += "%s " % errors[key][0]
            error_message = error_message.replace("This field", key.capitalize())
            error_message = error_message.replace("this field", key)
            error_message = error_message.replace("_", " ")
        error_message = error_message.strip()
        return error_message
