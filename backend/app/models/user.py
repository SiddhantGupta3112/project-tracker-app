from app import db
from datetime import datetime, timezone


class User(db.Model):
    from .team import Team
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # Relationships
    personal_team = db.relationship("Team", uselist=False, backref="owner", lazy=True)
    team_memberships = db.relationship("TeamMember", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

    def create_personal_team(self):
        if not self.personal_team:
            team = Team(
                team_name=f"{self.username}'s Personal Team",
                owner_id=self.id
            )
            db.session.add(team)
            db.session.commit()


