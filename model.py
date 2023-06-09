from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Quotes(db.Model):
    """Data model for a project."""

    __tablename__ = "Quotes"

    project_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project_name = db.Column(db.String(100), nullable=False)
    project_description = db.Column(db.String(500), nullable=False)
    budget = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Project project_id=%s project_name=%s>" % (self.project_id, self.project_name)