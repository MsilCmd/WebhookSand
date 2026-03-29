from flask import Flask, request, jsonify
import json
import hmac
import hashlib

app = Flask(__name__)

# Optional: secret for validating notifications
WEBHOOK_SECRET = "YOUR_SECRET_VALUE"

@app.route("/notifications", methods=["POST", "GET"])
def notifications():

    # STEP 1: Microsoft Graph validation handshake
    validation_token = request.args.get("validationToken")
    if validation_token:
        return validation_token, 200

    # STEP 2: Receive notifications
    data = request.get_json()

    # Optional: validate signature if you add one later
    # signature = request.headers.get("X-Hub-Signature")
    # if not validate_signature(signature, request.data):
    #     return "Invalid signature", 401

    print("Received notification:")
    print(json.dumps(data, indent=2))

    return jsonify({"status": "received"}), 202


def validate_signature(signature, payload):
    if not signature:
        return False
    mac = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha256)
    expected = "sha256=" + mac.hexdigest()
    return hmac.compare_digest(expected, signature)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
