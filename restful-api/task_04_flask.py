#!/usr/bin/python3
"""Simple API using python with Flask"""


from flask import Flask, request, jsonify


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Return a str in root path"""
    return "Welcome to the Flask API !"


@app.route('/data')
def list_users():
    """Return a list of users"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Return a str in status path"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return a user data"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonfy({"error": "User not found"}), 404


@app.route('/add_user', methods=['Post'])
def add_user():
    """Return, add or not a user"""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    users[data["username"]] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__man__":
    app.run(debug=True)
