from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BLOB, Column, ForeignKey, Integer, Table, Text
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.orm import relationship

db = SQLAlchemy(engine_options={'echo': True})

Bookmark_User_association_table = Table('bookmark_user_association', db.Model.metadata,
    Column('bookmark_id', Integer, ForeignKey('Bookmark.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('User.id'), primary_key=True)
)

class Bookmark(db.Model):
    __tablename__ = 'Bookmark'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(Text)
    link = Column(Text)
    archived_version = Column(BLOB)

class Reader(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text)
    bookmarks = relationship("Bookmark",
                             secondary=Bookmark_User_association_table)
