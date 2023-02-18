from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("tutorial.html")


@app.route("/about")
def about():
    return render_template("about.html")


app.run(debug=True)
