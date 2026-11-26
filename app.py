from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    pesan = ""

    if request.method == "POST":
        nama = request.form["nama"]
        pesan = "Halo, " + nama

    return render_template("index.html", pesan=pesan)

if __name__ == "__main__":
    app.run(debug=True)