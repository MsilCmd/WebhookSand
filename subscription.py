import requests
from msal import ConfidentialClientApplication
import datetime
import json

TENANT_ID = "YOUR_TENANT_ID"
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

# Change this to your public HTTPS endpoint
NOTIFY_URL = "https://your-ngrok-or-server-url/notifications"

SCOPES = ["https://graph.microsoft.com/.default"]

def get_token():
    app = ConfidentialClientApplication(
        client_id=CLIENT_ID,
        client_credential=CLIENT_SECRET,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}"
    )
    token = app.acquire_token_for_client(scopes=SCOPES)
    return token["access_token"]

def create_subscription():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    # Example: subscribe to new messages in a mailbox
    body = {
        "changeType": "created",
        "notificationUrl": NOTIFY_URL,
        "resource": "/users/YOUR_USER_ID/messages",
        "expirationDateTime": (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat() + "Z",
        "clientState": "secretClientValue"
    }

    resp = requests.post(
        "https://graph.microsoft.com/v1.0/subscriptions",
        headers=headers,
        data=json.dumps(body)
    )

    print("Subscription response:")
    print(resp.status_code)
    print(resp.text)


if __name__ == "__main__":
    create_subscription()
