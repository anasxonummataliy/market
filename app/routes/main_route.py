from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from app.models import Category, Product

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
@main_bp.route("/home")
def home_page():
    categories = Category.query.all()

    category_id = request.args.get("category_id")
    query = request.args.get("q")

    products_query = Product.query
    if category_id:
        products_query = products_query.filter_by(category_id=category_id)
    if query:
        products_query = products_query.filter(Product.title.ilike(f"%{query}%"))

    products = products_query.all()
    return render_template("home.html", products=products, categories=categories)


@main_bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)
