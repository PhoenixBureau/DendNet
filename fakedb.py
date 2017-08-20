import logging
import pickle


log = logging.getLogger(__name__)
db = {}


def retrieve(tag):
    global db
    url = db[tag]
    log.debug('retrieve %s %s', tag, url)
    return url


def store(tag, url):
    log.debug('store %s %s', tag, url)
    global db
    db[tag] = url
    save()
    

def bump(from_, what, to):
    log.debug('bump %s %s %s', from_, what, to)


extract_graph = None


def load(fn='data.db'):
    global db
    try:
        with open(fn) as f:
            data = pickle.load(f)
    except:
        log.exception('load %r failed', fn)
    else:
        db.update(data)


def save(fn='new.data.db'):
    global db
    try:
        with open(fn, 'w') as f:
            pickle.dump(db, f)
    except:
        log.exception('load %r failed', fn)


if __name__ == '__main__':
    logging.basicConfig()
    load()
