from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    """This view will find the data for the indicated station (by int)
    and return it in in a dictionary.
    :param station: int
    :param date: int
    :return: dict
    """
    temperature = 23
    return {"station": station,
            "date" : date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
