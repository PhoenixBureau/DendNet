from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/register")
def reg():
    return render_template('register.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

