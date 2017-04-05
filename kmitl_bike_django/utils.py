from django.contrib.admin import ModelAdmin
from django.db import models


class AbstractModel(models.Model):

    class Meta:
        abstract = True

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class AbstractAdmin(ModelAdmin):

    list_per_page = 50

    readonly_fields = ('created_date', 'updated_date')

    exclude = ('created_date', 'updated_date')


