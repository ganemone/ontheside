from app_factory import db


class ProjectUser(db.Model):
    __tablename__ = 'project_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    role = db.Column(db.Enum('owner', 'contributer', 'designer'))
