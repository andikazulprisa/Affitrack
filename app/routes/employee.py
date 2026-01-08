from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.permissions import role_required
from app.models.user import User
from app.extensions import db
from app.services.auth_service import hash_password
from app.services.user_service import (
    get_all_employees,
    delete_employee_by_id
)

employee_bp = Blueprint("employee", __name__)

# CREATE EMPLOYEE (OWNER ONLY)
@employee_bp.route("", methods=["POST"])
@jwt_required()
@role_required("owner")
def create_employee():
    data = request.get_json()

    user = User(
        email=data["email"],
        password_hash=hash_password(data["password"]),
        full_name=data["full_name"],
        role="employee"
    )

    db.session.add(user)
    db.session.commit()

    return {
        "message": "Employee created successfully"
    }, 201


# LIST EMPLOYEES (OWNER ONLY)   
@employee_bp.route("", methods=["GET"])  # /employees
@jwt_required()
@role_required("owner")
def list_employees():
    employees = get_all_employees()

    return jsonify([
        {
            "id": emp.id,
            "email": emp.email,
            "full_name": emp.full_name,
            "created_at": emp.created_at.isoformat()
        }
        for emp in employees
    ]), 200


# DELETE EMPLOYEE (OWNER ONLY)
@employee_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
@role_required("owner")
def delete_employee(user_id):
    user = delete_employee_by_id(user_id)

    if not user:
        return {"message": "Employee not found"}, 404

    return {
        "message": "Employee deleted successfully"
    }, 200
