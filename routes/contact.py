from flask import Blueprint, request, jsonify
from database import get_db
from datetime import datetime

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        print("✅ CONTACT DATA RECEIVED:", data)
        
        conn = get_db()
        conn.execute(
            "INSERT INTO contacts (name, email, message, sent_date) VALUES (?, ?, ?, ?)",
            (
                data.get('name'), 
                data.get('email'), 
                data.get('message'), 
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
        )
        conn.commit()
        conn.close()
        
        return jsonify({"success": True, "message": "Message sent successfully!"})
    except Exception as e:
        print("❌ CONTACT ERROR:", str(e))
        return jsonify({"success": False, "message": str(e)}), 500