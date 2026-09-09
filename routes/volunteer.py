from flask import Blueprint, request, jsonify
from database import get_db

volunteer_bp = Blueprint('volunteer', __name__)

@volunteer_bp.route('/api/volunteer', methods=['POST'])
def volunteer():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO volunteers (name, email, phone, skills) VALUES (?, ?, ?, ?)", 
                 (data.get('name'), data.get('email'), data.get('phone'), data.get('skills')))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "Volunteer registration successful!"})