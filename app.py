from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'big!secret'


@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run()
