from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route("/message", methods=["GET"])
def message_get():
    return jsonify({
        "status": "Hi from container!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

