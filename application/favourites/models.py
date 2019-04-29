from application import db

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                          db.ForeignKey('account.id'),
                          nullable=False)
    script_id = db.Column(db.Integer,
                          db.ForeignKey('script.id'),
                          nullable=False)

    def __init__(self, user_id, script_id):
        self.user_id = user_id
        self.script_id = script_id

    