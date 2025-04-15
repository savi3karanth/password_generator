from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

#Different route using the app.route decorator
@app.route("/bye")
def bye():
    return "Bye"

#Variable route using the app.route decorator
@app.route('/<name>')
def greet_with_root(name):
    #return f"Hello {name + 12}"     # We cannot concatenate the str with int
    return f"Hello {name + '12'}"

#Variable name with username route using the app.route decorator
@app.route('/username/<name>')
def greeting_with_username(name):
    return f"This will just print the username as name {name}"

##Variable name with username route and a digit after that using the app.route decorator
@app.route('/username/<name>/1')
def greeting_with_username_digit_after(name):
    return f"This will print the name after the user name ie {name} and the digit"

#Creating variable paths using the app.route decorator
@app.route('/pathname/<path:name>')
def greeting_with_path(name):
    return f"This will print the entire path after the name {name} "

#Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<float:number>')
def greeting_with_path_and_number(name, number):
    return f"This will print the you are {name} and {number} old."


if __name__ == "__main__":
    app.run(debug=True, port=5002)