
from flask import Blueprint, jsonify
from config import db

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/", methods=["GET"])
def get_products():
    products = []
    for p in db.products.find():
        p["_id"] = str(p["_id"])
        products.append(p)
    return jsonify(products)
