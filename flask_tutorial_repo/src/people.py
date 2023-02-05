import sqlalchemy as db
from flask import make_response, abort
from database import Base, engine, SessionLocal
from model import Person, people_schema, person_schema


Base.metadata.create_all(bind=engine)
session = SessionLocal()

def create(person):
    lname = person.get("lname")
    existing_person = session.query(Person).filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=session)
        session.add(new_person)
        session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with last name {lname} already exists")


def read_all():
    people = session.query(Person).all()
    return people_schema.dump(people)



def read_one(lname):
    person = session.query(Person).filter(Person.lname == lname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")


def update(lname, FirstName):
    existing_person = session.query(Person).filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = person_schema.load(FirstName, session=session)
        existing_person.fname = update_person.fname
        session.merge(existing_person)
        session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")

def delete(lname):
    existing_person = session.query(Person).filter(Person.lname == lname).one_or_none()

    if existing_person:
        session.delete(existing_person)
        session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")
