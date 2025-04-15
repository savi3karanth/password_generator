from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello World</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media0.giphy.com/media/H3WEXmLQJvtewD7Ptm/giphy.gif?cid=ecf05e47r4y7y3kvnqrghkn24mk4c5luvyk64qfs6f8m0tqh&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=500>')


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function


@app.route('/bye')
@make_bold
@make_underline
@make_italic
def bye():
    return 'Bye!'

#Different routes using the app.route decorator
@app.route('/username/<name>')
@app.route('/<name>')

#creating variable path and converting the path to and specified data type
@app.route('/<name>/<int:number>')
def greeting(name, number):
    return f"Hello {name} are you {number} years old"

if __name__ == '__main__':
    #run the app in debug mode to auto reload
    app.run(debug=True, port=5002)