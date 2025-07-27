from app import db

class TaskTag(db.Model):
    __tablename__ = 'task_tags'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    tag = db.Column(db.String(50), nullable=False)

    task = db.relationship('Task', backref=db.backref('tags', lazy=True))

    def __repr__(self):
        return f"<TaskTag {self.tag} for Task {self.task_id}>"
