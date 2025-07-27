from app import db

class Prerequisite(db.Model):
    __tablename__ = 'prerequisites'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    prerequisite_task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)

    # Optional: Define relationships (optional if you want easier navigation)
    task = db.relationship('Task', foreign_keys=[task_id], backref=db.backref('prerequisites', lazy='dynamic'))
    prerequisite = db.relationship('Task', foreign_keys=[prerequisite_task_id])

    def __repr__(self):
        return f"<Prerequisite Task {self.task_id} depends on {self.prerequisite_task_id}>"
