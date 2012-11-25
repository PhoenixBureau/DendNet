from os.path import exists
from memcache import Client
from sekrit import MEMCACHE_SOCKET


if exists(MEMCACHE_SOCKET):
  CACHE = Client(['unix:' + MEMCACHE_SOCKET], debug=True)
else:
  CACHE = Client(['127.0.0.1:11213'], debug=True)
S = CACHE.set
G = CACHE.get


def store_dec(s):
  def inner(tag, url):
    s(tag, url)
    S(tag, url)
  return inner


def retrieve_dec(r):
  def inner(tag):
    url = G(tag)
    if url is None:
      url = r(tag)
      S(tag, url)
    return url
  return inner

