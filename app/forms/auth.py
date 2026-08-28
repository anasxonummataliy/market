from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, ValidationError
from flask_bcrypt import check_password_hash

from app.models.user import User


class RegisterForm(FlaskForm):
    first_name = StringField(
        label="First Name",
        validators=[
            DataRequired(),
            Length(min=3),
            Regexp(
                regex=r"^[A-Za-z]+$", message="Only alphabetic characters are allowed."
            ),
        ],
    )
    last_name = StringField(
        label="Last Name",
        validators=[
            DataRequired(),
            Length(min=3),
            Regexp(
                regex=r"^[A-Za-z]+$", message="Only alphabetic characters are allowed."
            ),
        ],
    )
    username = StringField(
        label="Username",
        validators=[
            DataRequired(),
            Length(min=6),
            Regexp(
                r"^[A-Za-z0-9_]+$",
                message="Only letters, numbers and underscore allowed.",
            ),
        ],
    )
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(
                min=8, max=72, message="Password must be between 8 and 72 characters."
            ),
        ],
    )
    confirm = PasswordField(
        label="Repeat Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must be match."),
        ],
    )
    submit = SubmitField(label="Submit")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "This username is already taken. Please enter other username!"
            )


class LoginForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[
            DataRequired(),
            Length(min=6),
            Regexp(
                r"^[A-Za-z0-9_]+$",
                message="Only letters, numbers and underscore allowed.",
            ),
        ],
    )
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=8, max=72, message="Password must be 8 characters"),
        ],
    )
    submit = SubmitField(label="Submit")
