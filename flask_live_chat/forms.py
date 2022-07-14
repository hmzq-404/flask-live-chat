from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from .field_constraints import user_constraints, message_constraints, room_constraints


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        [
            validators.Length(
                min=user_constraints["username"]["min"],
                max=user_constraints["username"]["max"],
            )
        ],
    )
    password = PasswordField(
        "Password",
        [
            validators.Length(
                min=user_constraints["password"]["min"],
                max=user_constraints["password"]["max"],
            )
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        [
            validators.Length(
                min=user_constraints["password"]["min"],
                max=user_constraints["password"]["max"],
            ),
            validators.EqualTo("password", message="Password confirmation must match password.")
        ],
    )
    submit = SubmitField("Submit")



class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        [
            validators.Length(
                min=user_constraints["username"]["min"],
                max=user_constraints["username"]["max"],
            )
        ],
    )
    password = PasswordField(
        "Password",
        [
            validators.Length(
                min=user_constraints["password"]["min"],
                max=user_constraints["password"]["max"],
            )
        ],
    )
    submit = SubmitField("Submit")
