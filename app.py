from flask import Flask, render_template, request, redirect, url_for, flash
from model import db, Quotes
from forms import QuoteForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Customers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    """Show estimate form."""
    form = QuoteForm()
    if form.validate_on_submit():
        project_name = request.form.get('project_name')
        project_description = request.form.get('project_description')
        budget = request.form.get('budget')
        start_date = request.form.get('start_date')
        flash(f"Project {project_name} has been created!")
        return redirect(url_for('homepage'))
    else:
        flash("All fields are required!")
    return render_template('estimate.html', form=form)