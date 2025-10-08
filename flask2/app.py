from flask import Flask, render_template, request
import os
local_dir = os.path.dirname(__file__) + "/"

app=Flask(__name__)

#flask --app app --debug run

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)