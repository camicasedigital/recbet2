from flask import Blueprint, render_template, request
from .models import Bet
from . import db

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        bet = Bet(
            question1=request.form.get("q1"),
            question2=request.form.get("q2"),
            question3=request.form.get("q3")
        )
        db.session.add(bet)
        db.session.commit()
        return render_template("thanks.html")
    return render_template("index.html")
