from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, EqualTo, Email
from wtforms import DateField

class SignUp(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    email = StringField('email', validators=[Email(), InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired()])
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

class LogIn(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})

class UserData(FlaskForm):
    topic = SelectField('topics', choices=[('Alcohol', 'Alcohol'), ('AI', 'AI'), ('Bees', 'Bees'), ('Cyber Bullying', 'Cyber Bullying'), ('Sleep', 'Sleep'), ('Stress', 'Stress')])
    comment = StringField('comment', validators=[InputRequired()])
    submit = SubmitField('Submit', render_kw={'class': 'btn waves-effect waves-light white-text'})

