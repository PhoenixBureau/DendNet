import logging
from json import dumps
from flask import Flask, request, jsonify, render_template
from tags import tag_for
from openkeyvalue_store import retrieve, store


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


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', register_ajax='/regy')


@app.route("/regy", methods=['POST'])
def reg_ajax():
    url = request.form['urly']
    tag = tag_for(url)
    if store(**{tag: url}):
        log.info('register %s %r', tag, url)
        return jsonify(tag=tag)
    return 'error storing %r' % ({tag: url},)


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
    return render_template('bump.html', **data)


@app.route("/engage/<me>/<it>/<you>/")
def engage(me, it, you):
    if me != you:
        log.info('engage %s %s %s', me, it, you)
    return jsonify(result=True)


@app.route('/graph')
def graph():
    return render_template('graphlog.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

