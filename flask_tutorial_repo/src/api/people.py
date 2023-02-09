from flask import make_response, abort
from persistence.database import Base, engine, session
from persistence.model import Person, people_schema, person_schema


# Establishing tables using metadata objects with respect to enginge
Base.metadata.create_all(bind=engine)


def create(person):
    """This function creates a new person with a first and last name
    """
    last_name = person.get("last_name")
    existing_person = session.query(Person).filter(
        Person.last_name == last_name).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=session)
        session.add(new_person)
        session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with last name {last_name} already exists")


def read_all():
    """This reads and shows all persons information exist in the database
    """
    people = session.query(Person).all()
    return people_schema.dump(people)


def read_one(last_name):
    """This reads only one person information in the database
    """
    person = session.query(Person).filter(
        Person.last_name == last_name).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {last_name} not found")


def update(last_name, FirstName):
    """It updates a person information based on his/her last name
    """
    existing_person = session.query(Person).filter(
        Person.last_name == last_name).one_or_none()

    if existing_person:
        update_person = person_schema.load(FirstName, session=session)
        existing_person.first_name = update_person.first_name
        session.merge(existing_person)
        session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with last name {last_name} not found")


def delete(last_name):
    """It deletes a person from the database
    """
    existing_person = session.query(Person).filter(
        Person.last_name == last_name).one_or_none()

    if existing_person:
        session.delete(existing_person)
        session.commit()
        return make_response(f"{last_name} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {last_name} not found")
