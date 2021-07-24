from flask import Flask, render_template
import decouple 

app = Flask(__name__)

name = "Mila"
contact = decouple.config("CONTACT_FORM_API", default=None)

@app.route("/")
def about():
  return render_template("about.html", name=name)

@app.route("/CV")
def CV():
  return render_template("CV.html", name=name)

@app.route("/contacts")
def contacts():
  return render_template("contacts.html", name = name, api = contact)