from app import db

class ProjectTask(db.Model):
    __tablename__ = 'project_tasks'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)

    project = db.relationship('Project', backref=db.backref('project_tasks', lazy=True))
    task = db.relationship('Task', backref=db.backref('project_links', lazy=True))

    def __repr__(self):
        return f"<ProjectTask Project {self.project_id}, Task {self.task_id}>"
