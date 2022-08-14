from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Length, InputRequired


class StartForm(FlaskForm):
    username = StringField('Enter your Nickname', validators=[Length(min=5, max=32), InputRequired()])
    # password = PasswordField('Пароль', validators=[Length(min=5, max=24), InputRequired()])
    # game_mode = RadioField()
    difficulty_level = RadioField('Choose difficulty level', choices=['easy', 'medium', 'hard'])
    submit = SubmitField('Start')
