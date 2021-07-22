from flask import Flask, render_template

app = Flask(__name__)
name = "Mila"
list_of_stuff = ["Blanket", "Pillow", "Puter"]

@app.route("/")
def about():
  return render_template("about.html", name=name,
  list_of_stuff = list_of_stuff)

@app.route("/projects")
def projects():
  return render_template("projects.html", name=name)

@app.route("/contacts")
def contacts():
  return render_template("contacts.html", name = name)