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

    def __init__(self, title, content, author_id, script_id):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.script_id = script_id

    