# WebhookSand
A sandbox for building webhooks
# Microsoft Graph Webhook Starter (Python)

This project provides a minimal Python webhook service for receiving
Microsoft Graph change notifications. It includes:

- A Flask webhook endpoint (`/notifications`)
- A subscription creator script (`subscription.py`)
- MSAL authentication for Graph API
- Support for validation tokens and optional HMAC signatures

## Features

- Handles Graph validation handshake
- Receives and logs notifications
- Easily extendable for SharePoint, Outlook, Teams, or OneDrive events
- Clean structure for building a full automation service

## Setup

1. Create an app registration in Entra ID:
   - Add a client secret
   - Add API permissions for the resource you want to subscribe to
   - Add `https://your-domain/notifications` as a webhook URL

2. Install dependencies:


