from flask import Flask

app = Flask(__name__)
from flask import render_template

@app.route("/mypage/me")
def me():
    return render_template("parent.html")

@app.route("/mypage/contact")
def contact():
    return render_template("child.html")