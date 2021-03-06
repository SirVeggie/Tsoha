from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):
    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    scripts = db.relationship("Script", backref='account', lazy=True)
    comments = db.relationship("Comment", backref='account', lazy=True)
    userroles = db.relationship("Userrole", backref='account', lazy=True)
    favourites = db.relationship("Favourite", backref='account', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        stmt = text("SELECT role FROM userrole WHERE user_id = " + str(self.id))
        res = db.engine.execute(stmt)

        roles = []
        for row in res:
            roles.append(row[0])

        return roles
    
    def is_admin(self):
        for role in self.roles():
            if role == "ADMIN":
                return True
        
        return False

    def get_favourites_as_scripts(self):
        stmt = text("SELECT script.* FROM script, favourite "
                    "WHERE script.id = favourite.script_id "
                    "AND favourite.user_id = " + str(self.id))
        res = db.engine.execute(stmt)

        return res

    @staticmethod
    def number_of_contributing_users():
        stmt = text("SELECT COUNT(DISTINCT account.id) FROM account "
                    "LEFT JOIN script ON account.id = script.author_id "
                    "LEFT JOIN comment ON account.id = comment.author_id "
                    "WHERE account.id = script.author_id "
                    "OR account.id = comment.author_id")
        res = db.engine.execute(stmt)

        return res.first()[0]

    @staticmethod
    def top_contributing_user():
        stmt = text("SELECT account.username, COUNT(script.id) FROM account, script "
                    "WHERE account.id = script.author_id "
                    "GROUP BY username "
                    "ORDER BY COUNT(script.id) DESC")
        res = db.engine.execute(stmt)

        return res.first()



class Userrole(db.Model):
    __tablename__ = "userrole"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(144), nullable=False)
    user_id = db.Column(db.Integer,
                          db.ForeignKey('account.id'),
                          nullable=False)

    def __init__(self, role, user_id):
        self.role = role
        self.user_id = user_id