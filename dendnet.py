from json import dumps
from flask import Flask, request, jsonify, render_template
from tags import tag_for
from openkeyvalue_store import retrieve, store


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/register")
def reg():
    return render_template('register.html',
        register_ajax='regy',
        register='regy',
        )


@app.route("/regy", methods=['POST'])
def reg_ajax():
    url = request.form['urly']
    tag = tag_for(url)
    if store(**{tag: url}):
        return jsonify(tag=tag)
    return 'error storing %r' % ({tag: url},)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

