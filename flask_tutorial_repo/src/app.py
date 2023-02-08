from flask import render_template
from config import connex_app, base_directory
from database import session
from model import Person


app = connex_app

app.add_api(base_directory / "swagger.yml")


@app.route("/")
def home():
    people = session.query(Person).all()

    return render_template("home.html", people=people)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000, debug=True)
