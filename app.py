from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><h1>Hello, World!</h1><button>Hello, World!</button>"
@app.route("/profile")
def profile():
    return "<p>Hello, profile!</p>" 
@app.route("/webapp")
def webapp():
    return "<p>Hello, webapp!</p>" 