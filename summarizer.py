from flask import Flask, request, jsonify, render_template,url_for
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")

def index():
    return render_template("index.html")
 
if __name__=="__main__":
    app.run()
