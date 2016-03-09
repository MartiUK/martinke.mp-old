from flask import Blueprint, render_template, send_from_directory
from flask_nav import Nav
from flask_nav.elements import Navbar, View

web = Blueprint('web', __name__, template_folder="templates",
                static_folder="static")


nav = Nav()
nav.register_element("web_top", Navbar(
    View("martinke.mp", ".index"),
    View("CV", ".static", filename="mk_resume-2016-03-09.pdf")
))


@web.route("/", methods=["GET"])
def index():
    return render_template('index.j2',
                           title="Martin Kemp - DevOps Specialist")
