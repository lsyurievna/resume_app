from flask import Flask, render_template
import decouple 
import os
from pathlib import Path
import markdown
import datetime

app = Flask(__name__)

name = "Mila"
contact = decouple.config("CONTACT_FORM_API")
  
@app.route("/")
def about():
  return render_template("layout.html", name=name)

@app.route("/contacts")
def contacts():
  return render_template("contacts.html", api = contact)
