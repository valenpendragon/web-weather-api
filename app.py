from flask import Flask, render_template, url_for
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data/stations.txt", skiprows=17)
columns = ["STAID", "STANAME                                 "]
stations = stations[columns]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    """This view will find the data for the indicated station (by int)
    and return it in in a dictionary.
    :param station: int
    :param date: int
    :return: dict
    """
    # Construct the filepath. The data is stored in the data directory,
    # a symbolic link to the actual data_small set. Windows and Flask seem to
    # have problems with relative pathing.
    path_from_root = "data/"
    file_stub = "TG_STAID"
    filepath = path_from_root + file_stub + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date" : date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
