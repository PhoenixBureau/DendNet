import os, logging
from json import dumps
from flask import Flask, request, jsonify, render_template
from tags import tag_for
from db import retrieve, store, bump as record_bump, extract_graph
from local_caching import store_dec, retrieve_dec


store = store_dec(store)
retrieve = retrieve_dec(retrieve)


def _setup_log():
    log = logging.getLogger('mon')
    log.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s'
        ))
    log.addHandler(sh)

    fh = logging.FileHandler('dendnet.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    log.addHandler(fh)

    return log


log = _setup_log()


TEMPLATES = os.environ.get('FLASK_TEMPLATES')
if TEMPLATES:
    assert os.path.exists(TEMPLATES), repr(TEMPLATES)
    app = Flask(__name__, template_folder=TEMPLATES)
else:
    app = Flask(__name__)
    app.debug = True


@app.route('/')
def index():
    return render_template('index.html', register_ajax='/regy')


@app.route("/regy", methods=['POST'])
def reg_ajax():
    url = request.form['urly']
    tag = tag_for(url)
    log.info('register %s %r', tag, url)
    try:
        store(tag, url)
    except:
        log.exception('register to db')
    return jsonify(tag=tag)


@app.route("/bump/<me>/<it>/")
def anonbumphook(me, it):
    return render_template('anonbumphook.html')


def anonbump(me, it):
    data = dict(
        register_ajax='/regy',
        from_url=retrieve(me),
        what_url=retrieve(it),
        me=me,
        it=it,
        )
    return render_template('anonbump.html', **data)


@app.route("/bump/<me>/<it>/<you>/")
def bump(me, it, you):
    if you == 'anon':
        return anonbump(me, it)
    data = dict(
        from_url=retrieve(me),
        iframe_url=retrieve(it),
        your_url=retrieve(you),
        me=me,
        it=it,
        you=you,
        )
    if me != you:
        log.info('bump %s %s %s', me, it, you)
        try:
            record_bump(me, it, you)
        except:
            log.exception('bump to db')
    return render_template('bump.html', **data)


@app.route("/engage/<me>/<it>/<you>/")
def engage(me, it, you):
    if me != you:
        log.info('engage %s %s %s', me, it, you)
    return jsonify(result=True)


@app.route("/reject/<me>/<it>/", methods=['POST'])
def reject(me, it):
    reason = request.form['reason'][:255]
    log.info('reject %s %s %r', me, it, reason)
    return jsonify(result=True)


@app.route('/rejected/')
def rejected():
    return render_template('rejected.html')


@app.route('/graph/<it>/')
def graph(it):
    nodes, links = extract_graph(it)
    return render_template('graphlog.html', nodes=nodes, links=links)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

