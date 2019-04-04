from application import db
from application.models import Base

class Script(Base):
    name = db.Column(db.String(144), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(30000), nullable=True)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('account.id'),
                          nullable=False)

    def __init__(self, name, language, content):
        self.name = name
        self.language = language
        self.content = content
