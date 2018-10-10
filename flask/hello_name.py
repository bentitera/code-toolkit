import flask
app = flask.Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1> Home <h1>
    <p> Here is the home page <\p>
    '''

@app.route('/greet/<name>')
def greet(name):
    return "Hello, {}!".format(name)