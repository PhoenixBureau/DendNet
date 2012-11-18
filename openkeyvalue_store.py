import requests


OKV = 'http://api.openkeyval.org/'


def store(**key_url):
  t = requests.post(OKV, data=key_url)
  return t.status_code == 200


def retrieve(key):
  r = requests.get(OKV + key)
  if r.status_code == 200:
    return r.text
  return ''
