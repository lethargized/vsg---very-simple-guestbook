from flask import Flask, render_template, make_response, request, redirect
import datetime, time
import html
import requests
app = Flask(__name__)

# changing this will change the title of the guestbook page, ideally
# you'd put name's guestbook, website's guestbook, etc
# please keep in mind this implementatation is very crude, and with no
# anti-spam protection. it's meant to be run on small, DIY websites
# and not on anything experiencing massive traffic
name = "vsg - very simple guestbook v.0.1.0"

# this is our comment database as a "flat" file (flat-file) database
# as its just simple comments we don't need anything more secure
# as self-explanatory names say, first one writes to database, the
# second one reads from it. [html.unescape('comment')].strip()
# is used to strip html tags, to prevent XSS. keep in mind
def write_to_file(data):
    comment = data[html.unescape('comment')].strip()
    if not comment:
        return
    with open("guests.db", "a") as file:
        file.write(f"{data['name']};{data['website']};{data['comment']};{data['timestamp']}\n")
def read_from_file():
    with open("guests.db", "r") as file:
        lines = file.readlines()
    return [line.strip().split(";") for line in lines]

# this here i a route for root, meaning the first thing that will load upon visiting 
# domain.ext, if you want for it to be on seperate page, change both @app.route("/guestbook")
# and return redirect("/guestbook") to desired location. eg /gb.
# don't attempt having it directly on root @app.route(/) as it tends to break on requests.
@app.route("/guestbook", methods=["GET", "POST"])
def index():
    # this here will actually write our comments aka guestbook entries
    # to the database
    if request.method == "POST": 
        data = request.form.to_dict()
        data["timestamp"] = str(datetime.datetime.now().strftime(" ―at %I:%M %p on %m/%d/%Y"))
        write_to_file(data)
        return redirect("/guestbook")
    # this here will display comments in order newest to latest
    # on the same page we left our comments
    comments = reversed(read_from_file())
    return render_template("guestbook.html", comments=comments, name=name)

# prevents someone from attmepting to do direct url access to retrive the db file,
# this won't prevent anything if they manage to get access to our server tho, so 
# remember: disable root, change ssh port, disable password login and only use ssh keys
# you can mix and match advices above as you see fit
@app.route("/guests.db")
def clever():
        return "nice try"

## a lil bit of trolling hurts no one :p
## i like adding things like this to my sites xD
@app.route("/admin")
@app.route("/wp-admin")
@app.route("/joomla/administrator")
@app.route("/drupal/admin")
@app.route("/administrator")
def troll():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if __name__ == '__main__':
    app.run(port=8080)
