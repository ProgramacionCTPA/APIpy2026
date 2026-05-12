from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import db

cart_bp = Blueprint("cart_bp", __name__)

@cart_bp.route("/", methods=["POST"])
@jwt_required()
def add():
    user = get_jwt_identity()
    db.cart.insert_one({"user_id": user["id"], "item_id": request.json["item_id"]})
    return jsonify({"msg": "added"})

@cart_bp.route("/", methods=["GET"])
@jwt_required()
def get_cart():
    user = get_jwt_identity()
    items = []
    for i in db.cart.find({"user_id": user["id"]}):
        i["_id"] = str(i["_id"])
        items.append(i)
    return jsonify(items)
