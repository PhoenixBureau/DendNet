import logging
from json import dumps
from flask import Flask, request, jsonify, render_template
from tags import tag_for
from openkeyvalue_store import retrieve, store


log = logging.getLogger('mon')


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/register")
def reg():
    return render_template(
        'register.html',
        register_ajax='regy',
        register='regy',
        )


@app.route("/regy", methods=['POST'])
def reg_ajax():
    url = request.form['urly']
    tag = tag_for(url)
    if store(**{tag: url}):
        log.info('register %s %r', tag, url)
        return jsonify(tag=tag)
    return 'error storing %r' % ({tag: url},)


@app.route("/bump/<me>/<it>/<you>")
def bump(me, it, you):
    data = dict(
        from_url=retrieve(me),
        iframe_url=retrieve(it),
        your_url=retrieve(you),
        me=me,
        it=it,
        you=you,
        )
    log.info('bump %s %s %s', me, it, you)
    return render_template( 'bump.html', **data)



if __name__ == '__main__':
    import sys
    logging.basicConfig(
        level=logging.DEBUG,
        stream=sys.stderr,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        )
    app.debug = True
    app.run(host='0.0.0.0')

