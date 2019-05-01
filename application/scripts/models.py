from application import db
from application.models import Base

class Script(Base):
    name = db.Column(db.String(144), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(30000), nullable=True)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('account.id'),
                          nullable=False)
    
    comments = db.relationship("Comment", backref='script', lazy=True)
    favourites = db.relationship("Favourite", backref='script', lazy=True)

    def __init__(self, name, language, content, author_id):
        self.name = name
        self.language = language
        self.content = content
        self.author_id = author_id
