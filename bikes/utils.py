import os

from django.utils import timezone


def thumbnail_file_name(instance, filename):
    extension = filename.split(".")[-1]
    now = timezone.now()
    return os.path.join("uploads",
                        now.strftime("%Y_%m_%d"),
                        "%s.%s" % (now.strftime("%H%M%S%f"), extension))
