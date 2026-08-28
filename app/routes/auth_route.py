from flask import Blueprint, flash, redirect, render_template, url_for
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user

from app.forms.auth import LoginForm, RegisterForm
from app.models import User, db


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        password = generate_password_hash(form.password.data).decode("utf-8")

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password_hash=password,
        )
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Registration successful!", 'success')

        return redirect(url_for("main.home_page"))
    return render_template("register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Login successful!", 'success')
            return redirect(url_for("main.home_page"))

        else:
            flash("Incorrect username or password.", "danger")

    return render_template("login.html", form=form)


@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", 'info')
