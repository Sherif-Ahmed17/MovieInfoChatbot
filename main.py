from flask import Flask, request, jsonify
import bot
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'Password'
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/chat", methods=["POST"])
def chat():
    if request.method == "POST":
        request_data = request.get_json()
        message = request_data['message']
        status, response = bot.chat(message)
        data = {}
        data["reply"] = response
        data["status"] = 'success' if status != 0 else 'failed'
        return jsonify(data)


if __name__ == "__main__":
    app.run()