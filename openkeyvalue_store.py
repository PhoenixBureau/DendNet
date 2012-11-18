import requests


OKV = 'http://api.openkeyval.org/'


CACHE = {}


def store(**key_url):
  CACHE.update(key_url)
  return requests.post(OKV, data=key_url).status_code == 200


def retrieve(key):
  value = CACHE.get(key)
  if value is not None:
    return value
  r = requests.get(OKV + key)
  if r.status_code == 200:
    return r.text
  return ''
