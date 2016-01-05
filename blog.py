#blog.py - controller

#imports
from flask import Flask, render_template, request, session, \
				  flash, redirect, url_for, g
import sqlite3

#configuration
DATABASE = 'blog.db'

app = Flask(__name__)

#pulls in app configuration by looking for uppercase variables(DATABASE)
app.config.from_object(__name__)

#function used to connect to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#functions for views
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

#runns the app
if __name__ == '__main__':
	app.run(debug=True)
