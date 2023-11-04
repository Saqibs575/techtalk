from blog.models import User
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms.validators import Email
from flask_login import current_user
from flask_wtf.file import FileField
from wtforms.validators import Length
from wtforms.validators import EqualTo
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError

class RegistrationForm(FlaskForm) :
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("ConfirmPassword", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username) :
        user = User.query.filter_by(username=username.data).first()
        if user :
            raise ValidationError("This username is already taken. Please provide other names.")
    def validate_email(self, email) :
        user = User.query.filter_by(username=email.data).first()
        if user :
            raise ValidationError("This email is already taken. Please provide other names.")
            
class LoginForm(FlaskForm) :
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

class UpdateProfileForm(FlaskForm) :
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    profile_pic = FileField("Edit Profile Image", validators=[FileAllowed(["jpeg", "jpg", "png"])])
    submit = SubmitField("Save Changes")

    def validate_username(self, username) :
        if username.data != current_user.username :
            user = User.query.filter_by(username=username.data).first()
            if user :
                raise ValidationError("This username is already taken. Please provide other names.")
    def validate_email(self, email) :
        if email.data != current_user.email :
            user = User.query.filter_by(email=email.data).first()
            if user :
                raise ValidationError("This email is already taken. Please provide other names.")

class UpdateProfileImageForm(FlaskForm) :
    profile_pic = FileField("Edit Profile Image", validators=[FileAllowed(["jpeg", "jpg", "png"])])

class PostForm(FlaskForm) :
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")