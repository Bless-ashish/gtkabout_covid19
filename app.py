from flask import Flask,render_template
import requests


app =Flask(__name__)

#Home page 
@app.route("/")
def home():
    return render_template("index.html")

#India
@app.route("/country")
def country():
    data =requests.get("https://disease.sh/v2/countries/india?yesterday=true&strict=true")
    data.dict = data.json()
    return render_template("country.html",data=data.dict)

#world
@app.route("/world")
def world():
    data1 =requests.get("https://corona.lmao.ninja/v2/all")
    data1.dict = data1.json()
    return render_template("world.html",data1=data1.dict)

#info
@app.route("/info")
def info():
    return render_template("info.html")


if __name__== "__main__":
    app.run(debug= True)
