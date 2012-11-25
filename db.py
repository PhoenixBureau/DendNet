from datetime import datetime
import psycopg2
from sekrit import SOOPER_SEKRIT_PASSWORD


db = psycopg2.connect(host='127.0.0.1',
                      database='calroc_dendrite',
                      user='calroc_dendrite',
                      password=SOOPER_SEKRIT_PASSWORD,)
db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)


def retrieve(tag):
  cursor = db.cursor()
  cursor.execute("""SELECT url FROM tags.tags WHERE tag = %s;""", (tag,))
  result = cursor.fetchone()
  return result[0] if result else ''


def store(tag, url):
  cursor = db.cursor()
  try:
    cursor.execute(
      """INSERT INTO tags.tags (tag, url) VALUES (%s, %s);""",
      (tag, url)
      )
  except psycopg2.IntegrityError:
    pass


def bump(from_, what, to):
  cursor = db.cursor()
  cursor.execute(
    """INSERT INTO tags.bumps ("when", "from", "what", "to") VALUES (%s, %s, %s, %s);""",
    (datetime.utcnow(), from_, what, to)
    )


def extract_graph(tag):
  cursor = db.cursor()
  cursor.execute(
    """SELECT "when", "from", "to" FROM tags.bumps WHERE "what" = %s;""",
    (tag,)
    )
  nodes, links = set(), []
  for when, from_, to in cursor.fetchall():
    nodes.update((from_, to))
    links.append((when, from_, to))
  return list(nodes), links


