from flask import Flask, render_template, request
from markupsafe import escape

app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/info")
def info():
    return "<h1> All About Me </h1>" + "<p> Favorite color is purple! </p>"

@app.route("/wrong/<game>")
def wrong(game):
    return render_template("index.html", game=escape(game))

@app.route("/form", methods=["GET","POST"])
def form():
    if request.method=="POST":
        app.logger.info(request.form.get("name"))
    return render_template("form.html")
