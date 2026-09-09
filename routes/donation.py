from flask import Blueprint, request, jsonify
from database import get_db
from datetime import datetime

donation_bp = Blueprint('donation', __name__)

@donation_bp.route('/api/donate', methods=['POST'])
def donate():
    try:
        data = request.json
        
        # Security: Card number ki sirf aakhri 4 digits save karein
        card_num = data.get('card_number', '')
        last_four = card_num[-4:] if len(card_num) >= 4 else ''

        conn = get_db()
        conn.execute("""
            INSERT INTO donations 
            (name, email, phone, city, amount, payment_method, card_number, card_expiry, card_cvv, transaction_date, status) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get('name'),
            data.get('email'),
            data.get('phone'),
            data.get('city'),
            data.get('amount'),
            data.get('payment_method'),
            last_four,
            data.get('card_expiry', ''),
            data.get('card_cvv', ''),
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Completed'
        ))
        conn.commit()
        conn.close()
        
        return jsonify({"success": True, "message": "Aapki donation successful ho gayi hai. JazakAllah!"})
        
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500