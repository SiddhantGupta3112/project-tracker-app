from app import db
from datetime import datetime, timezone

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    assigned_to_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    start_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime)
    
    status = db.Column(db.String(20), nullable=False, default='pending') 
    priority = db.Column(db.String(15), nullable=False, default='medium') 
    
    created_on = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_on = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))
    project = db.relationship('Project', backref=db.backref('tasks', lazy=True))

    def __repr__(self):
        return f"<Task {self.task_name} (Project ID: {self.project_id})>"
