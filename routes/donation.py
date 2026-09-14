from flask import Blueprint, request, jsonify
from database import get_db
from datetime import datetime
import random

donation_bp = Blueprint('donation', __name__)

@donation_bp.route('/api/donate', methods=['POST'])
def donate():
    try:
        data = request.json
        print("✅ DATA RECEIVED IN BACKEND:", data)  # <--- Yeh line add karein
        date_str = datetime.now().strftime('%Y%m%d')
        random_num = random.randint(10000, 99999)
        tx_id = f"RWT-{date_str}-{random_num}"
        card_num = data.get('card_number', '')
        last_four = card_num[-4:] if len(card_num) >= 4 else ''
        conn = get_db()
        conn.execute(
            "INSERT INTO donations (name, email, phone, city, amount, payment_method, card_number, card_expiry, card_cvv, transaction_date, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
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
            )
        )
        conn.commit()
        conn.close()
        ngo_details = {
            "bank_name": "Habib Bank Limited (HBL)",
            "account_title": "Roshni Welfare Trust",
            "account_no": "0123-4567-8901-23",
            "iban": "PK36 HABL 0000 0001 2345 6789",
            "jazzcash": "0300-1234567 (Title: Roshni Trust)",
            "easypaisa": "0345-9876543 (Title: Roshni Trust)"
        }
        return jsonify({
            "success": True,
            "message": "Aapki donation successful ho gayi hai. JazakAllah!",
            "transaction_id": tx_id,
            "ngo_details": ngo_details
        })
    except Exception as e:
        print("DATABASE ERROR: " + str(e))
        return jsonify({"success": False, "message": str(e)}), 500