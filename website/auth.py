from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@auth.route("/contact-me")
def contact_me():
    return render_template("contact_me.html")
