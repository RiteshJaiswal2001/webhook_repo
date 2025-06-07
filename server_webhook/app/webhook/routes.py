from flask import Blueprint, request, jsonify
from app.extensions import mongo
from datetime import datetime, timezone
import uuid

webhook = Blueprint("webhook", __name__, url_prefix="/webhook")

@webhook.route("/receiver", methods=["POST"])
def receiver():
    event_type = request.headers.get("X-GitHub-Event", "ping")
    # print(request)
    payload = request.json

    author = payload.get("sender", {}).get("login", "unknown")
    timestamp = datetime.now(timezone.utc).isoformat()
    from_branch = to_branch = "unknown"
    action = event_type.upper()

    if event_type == "push":
        to_branch = payload.get("ref", "").split("/")[-1]
        action = "PUSH"

    elif event_type == "pull_request":
        pr = payload.get("pull_request", {})
        from_branch = pr.get("head", {}).get("ref", "")
        to_branch = pr.get("base", {}).get("ref", "")
        if payload.get("action") == "closed" and pr.get("merged"):
            action = "MERGE"
        else:
            action = "PULL_REQUEST"

    data = {
        "request_id": str(uuid.uuid4()),
        "author": author,
        "action": action,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }
    # print (data)
    mongo.db.github_event.insert_one(data)
    return jsonify({"message": "Webhook received"}), 200

@webhook.route("/events", methods=["GET"])
def get_events():
    pipeline = [
    {"$sort": {"_id": -1}},  
    {"$group": {
        "_id": "$action",           
        "latest_event": {"$first": "$$ROOT"}  
    }},
    {"$replaceRoot": {"newRoot": "$latest_event"}},  
    {"$project": {"_id": 0}}  
    ]

    events = list(mongo.db.github_event.aggregate(pipeline))
    # print(events)
    return jsonify(events)



# @webhook.route("/test-db", methods=["GET"])
# def test_db():
#     try:
#         collections = mongo.db.list_collection_names()
#         return jsonify({"connected": True, "collections": collections}), 200
#     except Exception as e:
#         return jsonify({"connected": False, "error": str(e)}), 500
