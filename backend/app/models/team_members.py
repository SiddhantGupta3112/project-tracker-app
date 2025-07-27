from app import db
from datetime import datetime, timezone

class TeamMember(db.Model):
    __tablename__ = 'team_members'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='member')
    joined_on = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    
    user = db.relationship('User', backref=db.backref('team_memberships', lazy=True))
    team = db.relationship('Team', backref=db.backref('members', lazy=True))

    def __repr__(self):
        return f"<TeamMember user_id={self.user_id}, team_id={self.team_id}, role={self.role}>"
