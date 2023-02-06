from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from database import Base, engine
from config import ma
from datetime import datetime


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    lname = Column(String(32), unique=True)
    fname = Column(String(32))
    timestamp = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = Session(engine)

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)
