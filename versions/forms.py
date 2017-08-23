from django import forms

from kmitl_bike_django.settings import ANDROID_APP_URL, IOS_APP_URL
from versions.models import AndroidAppVersion, AppVersion, IosAppVersion


class AndroidAppVersionForm(forms.ModelForm):

    class Meta:
        model = AndroidAppVersion
        fields = ("platform", "version_code", "version_name", "url")

    def __init__(self, *args, **kwargs):
        super(AndroidAppVersionForm, self).__init__(*args, **kwargs)
        self.fields["platform"].initial = AppVersion.Platform.ANDROID
        self.fields["url"].initial = ANDROID_APP_URL


class IosAppVersionForm(forms.ModelForm):

    class Meta:
        model = IosAppVersion
        fields = ("platform", "version_code", "version_name", "url")

    def __init__(self, *args, **kwargs):
        super(IosAppVersionForm, self).__init__(*args, **kwargs)
        self.fields["platform"].initial = AppVersion.Platform.IOS
        self.fields["url"].initial = IOS_APP_URL
