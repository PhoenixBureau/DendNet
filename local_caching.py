from os.path import exists
from hashlib import md5
from dendnet.memcache import Client
from tagly import tag_for as gen_tag
from sekrit import MEMCACHE_SOCKET


if exists(MEMCACHE_SOCKET):
  CACHE = Client(['unix:' + MEMCACHE_SOCKET], debug=True)
else:
  CACHE = Client(['127.0.0.1:11213'], debug=True)


def store_dec(s):
  S = CACHE.set
  def inner(tag, url):
    s(tag, url)
    S(tag, url)
  return inner


def retrieve_dec(r):
  S = CACHE.set
  G = CACHE.get
  def inner(tag):
    url = G(tag)
    if url is None:
      url = r(tag)
      S(tag, url)
    return url
  return inner
