from flask import Flask, request, jsonify, render_template,url_for,redirect,session
from flask_bootstrap import Bootstrap
from wtforms import  StringField, SubmitField,TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import Required, Length, InputRequired
from chichingfak import Summary
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '^_^ I am the boss @_@'
bootstrap = Bootstrap(app)


class MyForm(FlaskForm):
    text_area = TextAreaField("Enter any Bengali Document here:",validators=[Required()])
    submit = SubmitField("SUMMARIZE")

@app.route("/",methods=["POST","GET"])
def index():
    form = MyForm()
    res = ""
    if form.validate_on_submit():
        doc = form.text_area.data
        obj = Summary(doc)
        res = obj.summarize()
        # session['summary'] = res
        # print(res)
        redirect(url_for('index'))
    return render_template("index.html",form=form,res=res)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def not_found(e):
    return render_template("500.html"), 500


if __name__=="__main__":
    app.run(debug=True)
