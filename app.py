from flask import Flask, render_template
import decouple 
import os
from pathlib import Path

app = Flask(__name__)

name = "Mila"
contact = decouple.config("CONTACT_FORM_API" )
blog_posts = []

#If a file in the blog dir has ".md" extension
#print its name
with os.scandir("blog") as it:
  for entry in it:
    if entry.name.endswith(".md") and entry.is_file():
      post_data = Path(entry.path).read_text()
      
      blog_posts.append({
        "name": entry.name,
        "data": post_data
      })
     

@app.route("/")
def about():
  return render_template("about.html", name=name)

@app.route("/CV")
def CV():
  return render_template("CV.html", name=name)

@app.route("/contacts")
def contacts():
  return render_template("contacts.html", name = name, api = contact)

@app.route("/blog_listing")
def blog_listing():
  return render_template("blog_listing.html", name = name, blog_posts = blog_posts)

@app.route("/blog_listing/<post_name>")
def blog_entry(post_name):
  return render_template("blog_entry.html", name = name, post_name = post_name)