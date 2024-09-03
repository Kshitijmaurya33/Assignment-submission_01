from flask import Flask, jsonify, render_template
from time_scraper import main

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getTimeStories", methods=["GET"])
def get_time_stories():
    latest_stories = main()
    return jsonify(latest_stories)

if __name__ == "__main__":
    app.run(debug=True)