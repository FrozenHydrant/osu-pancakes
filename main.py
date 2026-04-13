from flask import Flask
from osu import Client
from dotenv import load_dotenv
import os
import json
from util.sweetness_analyzer import SweetnessAnalyzer


# Setup
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

app: Flask = Flask(__name__)
target_sweetness_analyzer: SweetnessAnalyzer = SweetnessAnalyzer()
client: Client = Client.from_credentials(CLIENT_ID, CLIENT_SECRET, "https://127:0:0:1")


@app.route("/")
def read_root():
    return "Hello World"


@app.route("/test")
def test_route():
    data = {}
    all_scores_result = client.get_all_scores()
    for i, score in enumerate(all_scores_result.scores):
        score_data = {}
        score_data["beatmap_id"] = score.beatmap_id
        score_data["timestamp_string"] = str(score.ended_at)
        score_data["misses"] = score.statistics.miss

        data[i] = score_data
    return json.dumps(data)


if __name__ == "__main__":
    app.run()