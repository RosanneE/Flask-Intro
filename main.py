from flask import Flask

# Instantiating a Flask object by passing __name__ argument 
# to the Flask constructor
app = Flask(__name__)

# The route() decorator, @app.route(), binds a URL to a function
@app.route('/')

# Routes in Flask are mapped to Python functions
def hello_world():
    return 'Hello World!'

# This condition ensures that the run() method is called 
# only when main.py is run as the main program
if __name__ == '__main__':

		# debug=True enables the debugger, 
		# provides detailed traceback of the error
    app.run(debug=True)