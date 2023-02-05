from flask import render_template
from config import connex_app, basedir
from database import SessionLocal
from model import Person


app = connex_app

app.add_api(basedir / "swagger.yml")


@app.route("/")
def home():
    session = SessionLocal()
    people = session.query(Person).all()

    return render_template("home.html", people=people)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000, debug=True)