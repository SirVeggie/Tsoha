from application import db

class Script(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    author = db.Column(db.String(144), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(30000), nullable=True)


    def __init__(self, name, author, language, content):
        self.name = name
        self.author = author
        self.language = language
        self.content = content
