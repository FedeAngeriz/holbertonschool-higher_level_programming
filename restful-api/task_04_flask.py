#!/usr/bin/env python3

from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
      return jsonify(users)

@app.route("/status")
def status():
      return jsonify("OK")

@app.route("/users/<username>")
def user(username):
      user = users.get(username)
      if user:
            return jsonify(user)
      else:
            return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
        app.run(debug=True)
