from ast import Pass

from flask_bcrypt import check_password_hash
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app.forms.admin import LoginForm
from app.models import User, db, Product, Category
from app.utils.decarators import admin_required


admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/", methods=["GET", "POST"])
def admin_page():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for("admin.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        admin = User.query.filter_by(is_admin=True, username=username).first()

        if admin and check_password_hash(admin.password_hash, password):
            login_user(admin)
            flash("Admin sifatida kirdingiz!", "success")
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Login yoki parol xato, yoki siz admin emassiz.", "danger")

    return render_template("admin/login.html", form=form)


@admin_bp.route("/dashboard")
@login_required
@admin_required
def dashboard():
    users = User.query.all()
    products = Product.query.all()
    return render_template("admin/dashboard.html", users=users, products=products)


@admin_bp.route("/logout")
@login_required
@admin_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")

