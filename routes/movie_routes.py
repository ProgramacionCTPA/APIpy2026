from flask import Blueprint, request, jsonify
from config import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId

movie_bp = Blueprint("movie_bp", __name__)

def is_admin():
    user_id = get_jwt_identity()
    user = db.users.find_one({"_id": ObjectId(user_id)})
    #print("USER:", user)  # DEBUG
    return user and user.get("role") == "admin"

@movie_bp.route("/", methods=["GET"])
def get_movies():
    movies = []
    for m in db.movies.find():
        m["_id"] = str(m["_id"])
        movies.append(m)
    return jsonify(movies)

@movie_bp.route("/", methods=["POST"])
@jwt_required()
def create_movie():
    user_id = get_jwt_identity()

    #print("USER_ID:", user_id)
    #print("HEADERS:", request.headers)
    #print("RAW DATA:", request.data)

    user = db.users.find_one({"_id": ObjectId(user_id)})

    if not user or user.get("role") != "admin":
        return jsonify({"error": "Solo admin"}), 403

    data = request.get_json(force=True)
    print("JSON:", data)

    if not data.get("titulo"):
        return jsonify({"error": "Falta título"}), 400

    db.movies.insert_one(data)

    return jsonify({"msg": "Película creada"})