# Global Imports
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField,PasswordField
from wtforms.validators import DataRequired,InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    

class PropertyForm(FlaskForm):
    # Attributes
    title = StringField('Property Title', validators=[DataRequired()])
    rooms = StringField('Number of Rooms', validators=[DataRequired()])
    bathrooms = StringField('Number of Bathrooms', validators=[DataRequired()])
    type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])