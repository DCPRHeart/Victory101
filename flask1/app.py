from flask import Flask, render_template, request
from markupsafe import escape
import os
local_dir = os.path.dirname(__file__)

app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/info")
def info():
    about_me = [
        "Favorite color is Purple",
        "Favorite band is ACDC"
    ]
    return render_template("info.html")

@app.route("/form", methods=["GET","POST"])
def form():
    context = {
        'success': False
    }
    if request.method=="POST":
        # request.form -> {name, last}
        #printing first name
        app.logger.info(request.form.get("name"))
        first=request.form.get("name")
        last=request.form.get("last")
        color=request.form.get("color")
        band=request.form.get("band")
        food=request.form.get("food")
        f = open(local_dir + "/formdata.csv", "a")
        f.write(f"{last}, {first}, {color}, {band}, {food}\n")
        context["success"] = True
    
    return render_template("form.html", **context)
