from flask import Flask, render_template
import decouple 
import os
from pathlib import Path
import markdown
import datetime

app = Flask(__name__)

name = "Mila"
contact = decouple.config("CONTACT_FORM_API" )
blog_posts = []
name_to_blog_post = {}

#If a file in the blog dir has ".md" extension
#print its name
with os.scandir("blog") as it:
  for entry in it:
    if entry.name.endswith(".md") and entry.is_file():
      raw_post_date, post_name = entry.name.split("_")
      post_date = datetime.datetime.strptime(raw_post_date, "%Y-%m-%d")
      post_name = post_name.rstrip(".md")
      post_data = Path(entry.path).read_text()
      html = markdown.markdown(post_data)

      blog_posts.append({
        "name": post_name,
        "date": post_date,
        "html": html
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
  for post in blog_posts:
    if post_name == post["name"]:
      return render_template("blog_entry.html", name = name, post=post)
  return "Post not found"