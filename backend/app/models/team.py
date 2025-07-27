from app import db
from datetime import datetime, timezone

class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    team_description = db.Column(db.Text)

    created_on = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    is_active = db.Column(db.Boolean, default = True)

    user = db.relationship("User", backref = "owner_id")