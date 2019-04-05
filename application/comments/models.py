from application import db
from application.models import Base

class Comment(Base):
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(10000), nullable=False)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('account.id'),
                          nullable=False)
    script_id = db.Column(db.Integer,
                          db.ForeignKey('script.id'),
                          nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    