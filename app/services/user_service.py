from app.models.user import User
from app.extensions import db

def get_all_employees():
    return User.query.filter_by(role="employee").all()

def delete_employee_by_id(user_id):
    user = User.query.filter_by(id=user_id, role="employee").first()
    if not user:
        return None

    db.session.delete(user)
    db.session.commit()
    return user
