import hashlib
import os
import re

from django.utils import timezone


def thumbnail_file_name(instance, filename):
    extension = filename.split(".")[-1]
    now = timezone.now()
    return os.path.join("uploads",
                        now.strftime("%Y_%m_%d"),
                        "%s.%s" % (now.strftime("%H%M%S%f"), extension))


def is_mac_address(mac_address):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
        return True
    return False


class Sha256Hash(object):

    @staticmethod
    def hash(message):
        hash_obj = hashlib.sha256(message)
        hashed_message = hash_obj.hexdigest()
        return hashed_message