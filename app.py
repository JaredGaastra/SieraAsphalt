from flask import Flask, render_template, request, redirect, url_for
from model import db, connect_to_db
from forms import QuoteForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Customers'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_to_db(app)

@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    """Show estimate form."""
    form = QuoteForm()
    if request.method == 'POST':
        project_name = request.form.get('project_name')
        project_description = request.form.get('project_description')
        budget = request.form.get('budget')
        start_date = request.form.get('start_date')

        return redirect(url_for('estimate'))

    return render_template('estimate.html')