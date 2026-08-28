from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField(
        label="Category Name",
        validators=[DataRequired(), Length(min=2, max=100)],
    )
    submit = SubmitField(label="Save")
