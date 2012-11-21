from datetime import datetime
from collections import defaultdict
import requests


LOG_URL = 'http://denebii:5000/static/dendnet.log'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S,%f'


class Logan:

  def __init__(self):
    self.REGISTER = {}
    self.BUMPS = defaultdict(set)
    self.ENGAGES = defaultdict(set)
    self._dispatch = dict(
      register=self.register,
      bump=self.bump,
      engage=self.engage,
      )

  def process(self, line):
    dt = datetime.strptime(line[:23], DATE_FORMAT)
    args = line[24:].split()
    kind = args.pop(0)
    method = self._dispatch.get(kind)
    if method:
      method(dt, *args)

  def register(self, dt, tag, url, *bits):
    assert not bits, repr((url, bits)) # Space(s) in the URL!?
    self.REGISTER.setdefault(tag, url[2:-1])

  def bump(self, dt, from_, what, to):
    self.BUMPS[what].add((from_, to))

  def engage(self, dt, from_, what, to):
    self.ENGAGES[what].add((from_, to))

  def retrieve(self, tag):
    return self.REGISTER.get(tag, tag)


if __name__ == '__main__':
  from pprint import pprint


  data = requests.get(LOG_URL).text.splitlines(False)
  el = Logan()
  for line in data:
    el.process(line)


  pprint(el.REGISTER)
  print ; print
  pprint(dict(el.BUMPS))
  print ; print
  pprint(dict(el.ENGAGES))
  print ; print
