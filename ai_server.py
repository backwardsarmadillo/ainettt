from flask import Flask, request
import os
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Store messages and groups
messages = {}
groups = {}

# Authentication token
auth_token = "lmaoauthtoken"

class AINetwork(Resource):
    def get(self, group):
        if group not in groups:
            return {"error": "Group not found"}, 404

        return {"messages": messages[group]}

    def post(self, group):
        # Check authentication
        token = request.headers.get("Authorization")
        if token != auth_token:
            return {"error": "Unauthorized"}, 401

        # Create group if it doesn't exist
        if group not in groups:
            groups[group] = True
            messages[group] = []

        # Add message to group
        message = request.get_json(force=True)
        messages[group].append(message)
        return {"result": "Message received"}

api.add_resource(AINetwork, "/ainetwork/<string:group>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
