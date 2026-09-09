from flask import Blueprint, jsonify
from database import get_db

faq_bp = Blueprint('faq', __name__)

@faq_bp.route('/api/faqs', methods=['GET'])
def get_faqs():
    conn = get_db()
    faqs = conn.execute('SELECT * FROM faqs').fetchall()
    conn.close()
    return jsonify([dict(row) for row in faqs])

@faq_bp.route('/api/campaigns', methods=['GET'])
def get_campaigns():
    conn = get_db()
    campaigns = conn.execute('SELECT * FROM campaigns').fetchall()
    conn.close()
    return jsonify([dict(row) for row in campaigns])