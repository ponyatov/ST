import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = b'\x80<C\x83\xf7\xb3Z\xfa\xedu,>\xbc\xec\xa1\xb1\r@i\x8b\x91)\xe7\x1f\xaat\xa6\xfb\x13\xea\x14\xa1\x10\xc4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

HOST = os.getenv('HOST', '127.0.0.1')
PORT = os.getenv('PORT', 12345)
