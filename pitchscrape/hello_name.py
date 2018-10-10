import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/greet/<name>')
def greet(name):
    '''Say hello to your first parameter'''
    return "Hello, {}!".format(name)

if __name__ == '__main__':
    app.run(debug=True)
    
