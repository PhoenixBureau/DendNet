import logging
from datetime import datetime
import psycopg2
from sekrit import SOOPER_SEKRIT_PASSWORD


def get_conn():
  db = psycopg2.connect(
    host='127.0.0.1',
    database='calroc_dendrite',
    user='calroc_dendrite',
    password=SOOPER_SEKRIT_PASSWORD,
    )
  db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
  return db


db = get_conn()
log = logging.getLogger(__name__)


def get_cursor():
  global db
  try:
    return db.cursor()
  except:
    log.exception("Had a problem getting a cursor, retrying...")
    db = get_conn()
    return db.cursor()


def attempt(query, args):
  cursor = get_cursor()
  try:
    cursor.execute(query, args)
  except psycopg2.IntegrityError:
    # Pass this up as we should only encounter it (harmlessly) when
    # repeating a store() call.
    raise
  except:
    log.exception("execution of query failed, retrying: %r %r", query, args)
    cursor.execute(query, args)
  return cursor


def retrieve(tag):
  cursor = attempt('SELECT url FROM tags.tags WHERE tag = %s;', (tag,))
  result = cursor.fetchone()
  return result[0] if result else ''


def store(tag, url):
  try:
    attempt(
      'INSERT INTO tags.tags (tag, url) VALUES (%s, %s);',
      (tag, url)
      )
  except psycopg2.IntegrityError:
    # Ignore duplicates.
    pass


def bump(from_, what, to):
  attempt(
    'INSERT INTO tags.bumps ("when", "from", "what", "to")'
    ' VALUES (%s, %s, %s, %s);',
    (datetime.utcnow(), from_, what, to)
    )


def extract_graph(tag):
  cursor = attempt(
    """SELECT "when", "from", "to" FROM tags.bumps WHERE "what" = %s;""",
    (tag,)
    )
  nodes, links = set(), []
  for when, from_, to in cursor.fetchall():
    nodes.update((from_, to))
    links.append((when, from_, to))
  return list(nodes), links
