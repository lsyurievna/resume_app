from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def about():
  return render_template("about.html")

@app.route("/projects")
def projects():
  return render_template("projects.html")

@app.route("/contacts")
def contacts():
  return render_template("contacts.html")