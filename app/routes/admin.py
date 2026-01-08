from flask import Blueprint
from app.utils.permissions import role_required

admin_bp = Blueprint("admin", __name__)

# KHUSUS OWNER ISTRIKU TERCINTA
@admin_bp.route("/admin", methods=["GET"])
@role_required("owner")
def owner_dashboard():
    return {
        "message": "Welcome to the owner dashboard"
    }, 200


# KHUSUS OWNER DAN KARYAWAN
@admin_bp.route("/reports", methods=["GET"])
@role_required("owner", "employee")
def get_reports():
    return {
        "message": "Reports accessible to owner and employees"
    }, 200