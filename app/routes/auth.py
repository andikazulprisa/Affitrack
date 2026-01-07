from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from app.services.auth_service import hash_password, verify_password
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already registered"}), 400
    
    user = User(
        full_name=data["full_name"],
        email=data["email"],
        password_hash=hash_password(data["password"]),
        role="owner"
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not verify_password(data["password"], user.password_hash):
        return jsonify({"message": "Invalid credentials"}), 401
    
    token = create_access_token(identity=str(user.id))

    return {
        "access_token": token,
    }, 200