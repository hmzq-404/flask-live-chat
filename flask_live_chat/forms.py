from wtforms import Form, StringField, PasswordField, SubmitField, validators
from .field_constraints import user_constraints, message_constraints, room_constraints


class RegistrationForm(Form):
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
            validators.EqualTo("password")
        ],
    )
    submit = SubmitField("Submit")
