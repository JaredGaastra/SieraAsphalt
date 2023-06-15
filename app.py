from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from model import db, Quotes
from forms import QuoteForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Customers'

db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.app_context().push()

@app.route('/', methods=['GET', 'POST'])
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    """Show estimate form."""
    form = QuoteForm()
    if form.validate_on_submit():
        project_name = form.project_name.data
        project_description = form.project_description.data
        budget = form.budget.data
        start_date = form.start_date.data
        flash(f"Project {project_name} has been created!")
        return redirect(url_for('homepage'))
    else:
        flash("All fields are required!")
    return render_template('estimate.html', form=form)