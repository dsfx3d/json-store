import secrets
from . import API_KEY_LEN


def generateApiKey(k=API_KEY_LEN):
  return secrets.token_hex(k//2)