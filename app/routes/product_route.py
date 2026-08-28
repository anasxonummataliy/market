from flask import Blueprint, render_template
from flask_login import login_required, current_user

product_bp = Blueprint("product", __name__)


@product_bp.route("/")
@product_bp.route("/home")
def home_page():
    return render_template("home.html")


@product_bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)
