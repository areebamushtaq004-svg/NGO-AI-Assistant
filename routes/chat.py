from flask import Blueprint, request, jsonify
from ai_logic import get_ai_response

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get('message', '')
    
    # AI logic se pura data (text aur button) mangwaya
    response_data = get_ai_response(user_msg)
    
    # Frontend ko alag alag text aur button bhejo taake error na aaye
    return jsonify({
        "success": True,
        "reply": response_data["text"],  # Sirf text yahan aayega
        "button": response_data["button"] # Button alag se aayega
    })