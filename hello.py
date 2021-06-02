from flask import Flask

app = Flask(__name__)


def make_italic(function):
    def wrapper_function(name):
        return f'<em>{function(name)}</em>'
    return wrapper_function


def make_bold(function):
    def wrapper_function(name):
        return f'<b>{function(name)}</b>'
    return wrapper_function


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return "Bye!"


@app.route('/username/<name>')
@make_bold
@make_italic
def greet(name):
    return f'Hello  there {name}'


if __name__ == '__main__':
    app.run(debug=True)
