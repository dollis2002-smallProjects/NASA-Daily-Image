from flask import Flask, redirect, url_for, render_template, request
from solar import SpaceImage

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        date = request.form["date"]
        return redirect(url_for("spaceimage", date=date))
    else:
        return render_template("index.html")

@app.route("/<date>")
def spaceimage(date):
    image = SpaceImage(date)
    image_url = image.image_url
    exp = image.description
    datos = image.datos
    title = image.title
    date = date
    
    return render_template("results.html", **locals())

if __name__ == "__main__":
    app.run(debug=True)
    