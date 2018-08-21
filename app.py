'''
Created on Aug 20, 2018

@author: Yan
'''

from flask import Flask, render_template, url_for, redirect, flash
from api.forms import registrationform, loginform
app = Flask(__name__)
app.config['SECRET_KEY'] = '12d8822e1ace6826867e470a7c78f5c1'


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration Page', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginform()
    if form.validate_on_submit():
        if form.email.data == 'admin@site.com' and form.password.data == 'password':
            flash('you have been logged in!')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your details')
    return render_template('login.html', title='Login Page', form=form)