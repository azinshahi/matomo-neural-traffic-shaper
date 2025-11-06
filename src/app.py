from flask import Flask, jsonify, request
from matomo_connector import MatomoConnector

app = Flask(__name__)

# Temporary placeholders
MATOMO_URL = "https://your-matomo-url.com"
MATOMO_TOKEN = "your_api_token"
SITE_ID = "1"

@app.route("/")
def index():
    return jsonify(message="Matomo Neural Traffic Shaper is running")

@app.route("/live")
def live_data():
    connector = MatomoConnector(MATOMO_URL, MATOMO_TOKEN)
    data = connector.get_live_data(SITE_ID)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
