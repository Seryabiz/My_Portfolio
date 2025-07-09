from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def Home():
    return "Welcome to my Home page"