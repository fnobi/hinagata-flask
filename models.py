from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from app import db

class Result(db.Model):
    """
    生成結果のモデル
    """

    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    uuid = Column(Unicode(255))
    name = Column(Unicode(255))
    score = Column(Integer)

    def __init__(name, score):
        self.uuid = uuid.uuid4()
        self.name = name.title()
        self.score = score.title()
