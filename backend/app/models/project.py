from app import db
from datetime import datetime, timezone

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(80), nullable=False)
    project_description = db.Column(db.Text, nullable=False)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

    start_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime)
    updated_on = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    is_archived = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(15), nullable=False)

    created_on = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    team = db.relationship("Team", backref="projects", lazy=True)
    tasks = db.relationship("Task", backref="project", lazy=True)

    def __repr__(self):
        return f"<Project {self.project_name}>"


