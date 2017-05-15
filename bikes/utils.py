import base64
import os
import re

import six
from Crypto.PublicKey import RSA
from django.utils import timezone

from kmitl_bike_django.settings import BASE_DIR


def thumbnail_file_name(instance, filename):
    extension = filename.split(".")[-1]
    now = timezone.now()
    return os.path.join("uploads",
                        now.strftime("%Y_%m_%d"),
                        "%s.%s" % (now.strftime("%H%M%S%f"), extension))


def is_mac_address(x):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", x.lower()):
        return True
    return False


class RSAEncryption(object):

    PRIVATE_KEY_FILE_PATH = os.path.join(BASE_DIR, "keys", "private.key")
    PUBLIC_KEY_FILE_PATH = os.path.join(BASE_DIR, "keys", "public.key")

    def encrypt(self, message):
        public_key = self._get_public_key()
        public_key_object = RSA.importKey(public_key)
        random_phrase = "M"
        encrypted_message = public_key_object.encrypt(self._to_format_for_encrypt(message), random_phrase)[0]
        return base64.b64encode(encrypted_message)

    def decrypt(self, encoded_encrypted_message):
        encrypted_message = base64.b64decode(encoded_encrypted_message)
        private_key = self._get_private_key()
        private_key_object = RSA.importKey(private_key)
        decrypted_message = private_key_object.decrypt(encrypted_message)
        return six.text_type(decrypted_message, encoding="utf8")

    def _get_public_key(self):
        with open(self.PUBLIC_KEY_FILE_PATH, "r") as _file:
            return _file.read()

    def _get_private_key(self):
        with open(self.PRIVATE_KEY_FILE_PATH, "r") as _file:
            return _file.read()

    @staticmethod
    def _to_format_for_encrypt(value):
        return str(value).encode("utf-8")
