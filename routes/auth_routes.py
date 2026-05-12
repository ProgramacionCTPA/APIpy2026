from flask import Blueprint, request, jsonify
from config import db
import bcrypt
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    role = data.get("role", "user")  # default user
    db.users.insert_one({"email": data["email"], "password": hashed, "role": role})
    return jsonify({"msg": "user created"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = db.users.find_one({"email": data["email"]})
    if user and bcrypt.checkpw(data["password"].encode(), user["password"]):
        token = create_access_token(identity=str(user["_id"]))
        return jsonify({"token": token, "role": user["role"]})
    return jsonify({"error": "invalid"}), 401
