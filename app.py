import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "My name is S Harsh and USN 1BM20IS219"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
