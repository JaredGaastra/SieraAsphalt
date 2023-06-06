from flask import Flask, render_template, request, redirect, url_for
from model import db, connect_to_db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Customers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_to_db(app)

@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')
