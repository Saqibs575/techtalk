import pytz
from blog import db
from datetime import datetime
from blog import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id) :
    return User.query.get(int(user_id))

class User(db.Model, UserMixin) :
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    profile_image = db.Column(db.String(20), nullable=False, default="profile_default.jpg")
    password = db.Column(db.String(50), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self) :
        return f"{self.username}"

class Post(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def formatted_date(self):
        IST = self.date_added.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Kolkata'))
        return IST.strftime("%I:%M:%p   %d/%m/%Y")

    def __repr__(self) :
        return f"{self.title}"