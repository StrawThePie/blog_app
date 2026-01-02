from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    articles = [
        {"id": 1, "title": "First Post", "published": "2026-01-01"},
        {"id": 2, "title": "Second Post", "published": "2030-01-02"},
    ]
    return render_template("home.html", articles=articles)


if __name__ == "__main__":
    app.run(debug=True)