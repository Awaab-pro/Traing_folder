from flask import Flask
app = Flask(__name__)

@app.route('/say_hello1/<x>')
def say_hello1(x):
    return ('Hello ' + x)
app.run()