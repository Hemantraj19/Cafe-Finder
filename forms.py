from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL


class AdminForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    login_button = SubmitField("Login")


class AddCafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    seats = SelectField(
        "Seats",
        choices=[
            ("0-10", "0-10"),
            ("10-20", "10-20"),
            ("20-30", "20-30"),
            ("30-40", "30-40"),
            ("50+", "50+"),
        ],
    )
    has_wifi = SelectField("Wifi", choices=[(1, "Yes"), (0, "No")])
    has_sockets = SelectField("Sockets", choices=[(1, "Yes"), (0, "No")])
    has_toilet = SelectField("Toilet", choices=[(1, "Yes"), (0, "No")])
    can_take_calls = SelectField("Calls", choices=[(1, "Yes"), (0, "No")])
    submit = SubmitField("Submit")
