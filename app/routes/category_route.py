from flask_login import login_required, current_user
from flask import Blueprint, render_template, flash, redirect, url_for

from app.forms.category import CategoryForm
from app.utils.decarators import admin_required
from app.models import User, Category, db

category_bp = Blueprint("category", __name__)


@category_bp.route("/categories")
@login_required
def categories():
    all_categories = Category.query.all()
    return render_template("admin/categories.html", categories=all_categories)


@category_bp.route("/category/create", methods=["GET", "POST"])
@login_required
@admin_required
def create_category():
    form = CategoryForm()

    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
            slug=form.name.data.lower().replace(" ", "-"),
        )
        db.session.add(category)
        db.session.commit()
        flash("Kategoriya qo'shildi!", "success")
        return redirect(url_for("category.categories"))

    return render_template("admin/create_category.html", form=form)


@category_bp.route("/category/<int:id>/edit", methods=["GET", "POST"])
@login_required
@admin_required
def update_category(id):
    category = Category.query.get_or_404(id)
    form = CategoryForm(obj=category)

    if form.validate_on_submit():
        category.name = form.name.data
        category.slug = form.name.data.lower().replace(" ", "-")
        db.session.commit()

        flash("Kategoriya yangilandi!", "success")
        return redirect(url_for("category.categories"))

    return render_template("admin/edit_category.html", form=form)


@category_bp.route("/category/<int:id>/delete", methods=["GET", "POST"])
@login_required
@admin_required
def delete_category(id):
    category = Category.query.get_or_404(id)

    if category.products:
        flash(
            "Bu kategoriyada mahsulotlar bor, avval ularni o'chiring yoki boshqa kategoriyaga ko'chiring.",
            "danger",
        )
        return redirect(url_for("category.categories"))

    db.session.delete(category)
    db.session.commit()
    flash("Kategoriya o'chirildi.", "success")
    return redirect(url_for("category.categories"))
