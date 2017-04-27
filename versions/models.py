from django.db import models

from kmitl_bike_django.utils import AbstractModel


class AppVersion(AbstractModel):

    class Meta:
        verbose_name = "Mobile Application Version"
        verbose_name_plural = "Mobile Application Versions"

        abstract = True

    class Platform(object):
        ANDROID = "Android"
        IOS = "iOS"

    platform = models.CharField("Platform", max_length=8, null=False, blank=False)
    version_code = models.CharField("Version code", max_length=32, null=False, blank=False, unique=True)
    version_name = models.CharField("Version name", max_length=32, null=False, blank=True)

    def __str__(self):
        return self.version_name


class AndroidAppVersionManager(models.Manager):

    def get_queryset(self):
        return super(AndroidAppVersionManager, self).get_queryset().filter(content_type=AppVersion.Platform.ANDROID)


class AndroidAppVersion(AppVersion):

    class Meta:
        verbose_name = "Android Application Version"
        verbose_name_plural = "Android Application Versions"

    objects = AndroidAppVersionManager()

    def __init__(self, *args, **kwargs):
        self._meta.get_field("platform").default = AppVersion.Platform.ANDROID
        super(AndroidAppVersion, self).__init__(*args, **kwargs)


class IosAppVersionManager(models.Manager):

    def get_queryset(self):
        return super(IosAppVersionManager, self).get_queryset().filter(content_type=AppVersion.Platform.IOS)


class IosAppVersion(AppVersion):

    class Meta:
        verbose_name = "iOS Application Version"
        verbose_name_plural = "iOS Application Versions"

    objects = IosAppVersionManager()

    def __init__(self, *args, **kwargs):
        self._meta.get_field("platform").default = AppVersion.Platform.IOS
        super(IosAppVersion, self).__init__(*args, **kwargs)
