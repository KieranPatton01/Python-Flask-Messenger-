from flask import Flask, render_template, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
#import email_validator
import sqlite3
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

#class RegistrationForm(FlaskForm):

   #nickname = StringField('nickname',
            #validators=[DataRequired(), Length(min=2, max=12)])
    
   #email = StringField('email',
            #validators=[DataRequired()])

   #password = PasswordField('password',
            #validators=[DataRequired(), Length(min=3, max=30)])

   #confirmPassword = PasswordField('conPassword',
            #validators=[DataRequired(), EqualTo('password')])
    
   #submit = SubmitField('button')

@app.route('/', methods=["GET", "POST"])
def reg():
    #if register is pressed..
    if request.method == 'POST':
        # message = "sumitted"

         connection = sqlite3.connect('var/sqlite3.db')
         cursor = connection.cursor()
         
         nickname = request.form['nickname']
         email = request.form['email']
         password = request.form['password']
         conPassword = request.form['conPassword']

         if password != conPassword:
             flash('You passwords do not match')
         return render_template('register.html')

         if password == conPassword:
             return redirect("http://webtech-45.napier.ac.uk:5000/login.py", code=302)

    return render_template('register.html')

if __name__ == "__main__":
    app.run(run)
