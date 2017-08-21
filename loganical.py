from datetime import datetime
from collections import defaultdict
import json


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
    self.BUMPS[from_, what].add((dt, to))

  def engage(self, dt, from_, what, to):
    self.ENGAGES[what].add((from_, to))

  def retrieve(self, tag):
    return self.REGISTER.get(tag, tag)


class JSONMixin:

  def bump(self, dt, from_, what, to):
    if from_ == to:
      return
    self.BUMPS[self.retrieve(what)].add(tuple(map(self.retrieve, (from_, to))))

  def engage(self, dt, from_, what, to):
    if from_ == to:
      return
    self.ENGAGES[self.retrieve(what)].add(tuple(map(self.retrieve, (from_, to))))

  def _post(self):
    self.BUMPS = dict((k, list(v)) for k, v in self.BUMPS.iteritems())
    self.ENGAGES = dict((k, list(v)) for k, v in self.ENGAGES.iteritems())


class JSONLogan(JSONMixin, Logan):
  pass


if __name__ == '__main__':
  import fileinput
  from pprint import pprint

  el = JSONLogan()
  for line in fileinput.input():
    el.process(line)
  el._post()

  pprint(json.dumps(el.REGISTER.values()))
  print ; print 'Bumps:'
  print json.dumps(el.BUMPS, indent=2)
  print ; print 'Engages:'
  print json.dumps(el.ENGAGES, indent=2)
  print ; print
