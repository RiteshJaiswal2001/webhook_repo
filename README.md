# 🚀 GitHub Webhook Receiver

A full-stack project that listens to GitHub webhook events like **Push**, **Pull Request**, and **Merge**, stores the event data in **MongoDB**, and displays it in real-time through a **React** frontend. The frontend polls the backend every 15 seconds to show the latest activity in a clean and minimal UI.

---

## 🧰 Tech Stack

### 🖥 Frontend

- **React.js** – For building a dynamic and responsive UI
- **Tailwind CSS** – For fast and elegant styling
- **Polling (every 15s)** – To keep the UI updated with latest events

### 🌐 Backend

- **Flask** – For handling incoming GitHub webhooks
- **Blueprints** – For modular route management
- **PyMongo** – MongoDB client for Python
- **Flask-CORS** – To enable frontend-backend communication
- **UUID** – For generating unique event IDs

### 🗃 Database

- **MongoDB** – NoSQL database for storing webhook event data

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Node.js and npm
- Python 3.x and pip
- MongoDB (running locally or remotely)
- [ngrok](https://ngrok.com/) – to expose localhost for webhook testing

---

## 🔧 Backend Setup

- Navigate to the backend folder:
  ```bash
  cd server_webhook
  ```
- And follow the instruction of READEME.md file of that folder.

## 🎨 Frontend Setup

1. Navigate to the frontend folder:
   ```bash
   cd client
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend app:
   ```bash
   npm run dev
   ```

## 🌍 Exposing Local Server using Ngrok

Since GitHub needs a public URL to send webhooks, we use **ngrok** to expose our local Flask server.

1. Download [ngrok](https://ngrok.com/) and install it.

2. Start ngrok on port **5000** (Flask default):
   ```bash
   ngrok http 5000
   ```
3. Copy the HTTPS forwarding URL from ngrok (e.g., https://abc123.ngrok.io)

## 🔗 Register GitHub Webhook

1. Go to your GitHub repo → Settings → Webhooks → Add webhook

2. Set Payload URL as:

   ```
   https://<your-ngrok-subdomain>.ngrok.io/webhook/receiver
   ```

3. Content type: application/json

4. Choose the events you want:

   - Push
   - Pull Request
   - Merge (via push/PR hooks)

5. Save webhook.
   - Now GitHub will send data to your Flask app every time those events happen.

## 🖥 UI Behavior

- The React app polls the backend every 15 seconds using Fetch.

- Displays a clean, responsive table or list of:

  - Event type (Push, PR, Merge)

  - Repository name

  - Sender name

  - Timestamp

## ✅ Features

    - GitHub Webhook listener and event recorder

    - Clean React UI to view all events

    - MongoDB persistence

    - Polling every 15 seconds to auto-refresh UI

    - Modular Flask backend using Blueprints
