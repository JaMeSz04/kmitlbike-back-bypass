from django.db import models

from kmitl_bike_django.utils import AbstractModel


class AppVersion(AbstractModel):

    class Meta:
        verbose_name = "Mobile Application Version"
        verbose_name_plural = "Mobile Application Versions"
        unique_together = ("platform", "version_code")

    class Platform(object):
        ANDROID = "Android"
        IOS = "iOS"

    _type = (
        (Platform.ANDROID, "Andriod"),
        (Platform.IOS, "iOS")
    )

    platform = models.CharField("Platform", max_length=8, null=False, blank=False, choices=_type)
    version_code = models.CharField("Version code", max_length=32, null=False, blank=False)
    version_name = models.CharField("Version name", max_length=32, null=False, blank=True)
    url = models.URLField("URL", null=False, blank=False)

    def __str__(self):
        return self.version_name

    @staticmethod
    def autocomplete_search_fields():
        return "version_code", "version_name"


class AndroidAppVersionManager(models.Manager):

    def get_queryset(self):
        return super(AndroidAppVersionManager, self).get_queryset().filter(platform=AppVersion.Platform.ANDROID)


class AndroidAppVersion(AppVersion):

    def __init__(self, *args, **kwargs):
        super(AndroidAppVersion, self).__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Android Application Version"
        verbose_name_plural = "Android Application Versions"
        proxy = True

    objects = AndroidAppVersionManager()


class IosAppVersionManager(models.Manager):

    def get_queryset(self):
        return super(IosAppVersionManager, self).get_queryset().filter(platform=AppVersion.Platform.IOS)


class IosAppVersion(AppVersion):

    def __init__(self, *args, **kwargs):
        super(IosAppVersion, self).__init__(*args, **kwargs)

    class Meta:
        verbose_name = "iOS Application Version"
        verbose_name_plural = "iOS Application Versions"
        proxy = True

    objects = IosAppVersionManager()

