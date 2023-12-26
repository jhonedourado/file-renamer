from flask import Flask, render_template, request
from app.main import rename

app = Flask(__name__)

@app.route("/")
@app.route("/", methods=["POST"])
def index():
  return render_template("index.html")

@app.route("/newName", methods=["POST"])
def newName():
  fileName = request.form.get("fileName")
  newName = rename(fileName)
  return render_template("newName.html", newName=newName)
