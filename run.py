from flask import Flask, render_template, request
from app.main import rename

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/newName", methods=["POST"])
def newName():
  fileName = request.form.get("fileName")
  newName = rename(fileName)
  return newName
