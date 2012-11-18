from json import dumps
from flask import Flask, jsonify, render_template
from tags import tag_for


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


@app.route("/regy")
def reg_ajax(request):
    assert request.method == 'POST'
    url = request.form['urly']
    tag = tag_for(url)
    return jsonify(tag=tag)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

