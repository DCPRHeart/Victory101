from flask import Flask, render_template, request
from markupsafe import escape
import uuid
import json
import os
local_dir = os.path.dirname(__file__) + "/"

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
        first=request.form.get("name")
        last=request.form.get("last")
        color=request.form.get("color")
        band=request.form.get("band")
        food=request.form.get("food")
        id = str(uuid.uuid4())
        ans={
            "id": id,
            "first": first,
            "last": last,
            "color": color,
            "band": band,
            "food": food
        }
        app.logger.info(ans)
        
        with open(local_dir+"data.json", "r+") as file:
            try:
                storage: dict = json.load(file)
            except json.JSONDecodeError:
                storage = {
                    "StorageData": []
                }
            arr: list =storage.get("StorageData",[])
            arr.append(ans)
            storage["StorageData"] = arr
            file.seek(0)
            json.dump(storage, file, indent=4)
            
        context["success"] = True
    
    return render_template("form.html", **context)


@app.route("/user/directory")
def user_directory():
    #Lists all users who have filled out the form
    #allow navigation to info about the user

    with open(local_dir+"data.json", "r") as file:
        try:
            storage: dict = json.load(file)
        except json.JSONDecodeError:
            storage = {
                "StorageData": []
            }
    users: list =storage.get("StorageData")
    
    return render_template("user/index.html", users=users)

@app.route("/user/info/<ID>")
def user_info(ID):
    context = {
        "user" : {"id": "", "first": "", "last": "", "color": "", "band": "", "food": ""}
    }
    #TODO: Read user info from data.json
    #
    #if ID in data.json StorageData
    #   Display user information
    #
    # else: say "User not Found"

    with open(local_dir+"data.json", "r") as file:
        try:
            storage: dict = json.load(file)
        except json.JSONDecodeError:
            storage = {
                "StorageData": []
            }
        users: list =storage.get("StorageData")
    
    found = None
    for user in users:
        if user["id"] == ID:
            found = user
            break
    #handle user not found:
    
    
    #handle user found:
    context["user"] = found

    return render_template("user/info.html", **context)
