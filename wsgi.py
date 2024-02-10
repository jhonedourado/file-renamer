from flask import Flask, render_template, request
from app.main import rename

app = Flask(__name__)

@app.route("/")
@app.route("/", methods=["POST"])
def index():
  return render_template("index.html")

@app.route("/new-name", methods=["POST"])
def new_name():
  file_name = request.form.get("file-name")
  new_name = rename(file_name)
  return render_template("new-name.html", new_name=new_name)
