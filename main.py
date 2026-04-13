from flask import Flask


# Setup
app: Flask = Flask(__name__)


@app.route("/")
def read_root():
    return "Hello World"


if __name__ == "__main__":
    app.run()