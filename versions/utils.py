from packaging.version import Version, InvalidVersion

from versions.models import AppVersion


def requires_update(platform, current_version):
    current_version = Version(current_version)
    try:
        latest_version = get_latest_version(platform)
        latest_version = Version(latest_version)

        if platform == AppVersion.Platform.ANDROID:
            url = "https://play.google.com/store/apps/details?id=com.bike.kmitl.kmitlbike"
        elif platform == AppVersion.Platform.IOS:
            url = "https://itunes.apple.com/th/app/kmitl-bike/id1133585302"
        else:
            url = "https://www.google.com/search?q=platform+not+supported"
        if current_version < latest_version:
            return True, url
        else:
            return False, None
    except InvalidVersion:
        return False, None


def get_latest_version(platform):
    try:
        app_version = AppVersion.objects.filter(platform=platform).last()
        return app_version.version_code
    except AppVersion.DoesNotExist:
        return None
