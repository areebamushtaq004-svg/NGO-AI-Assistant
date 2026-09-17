import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from database import init_db, get_db
from routes import chat, donation, faq, volunteer, contact

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

# Register Blueprints
app.register_blueprint(chat.chat_bp)
app.register_blueprint(donation.donation_bp)
app.register_blueprint(faq.faq_bp)
app.register_blueprint(volunteer.volunteer_bp)
app.register_blueprint(contact.contact_bp)

# Database har baar initialize ho (local aur server dono par)
init_db()

@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')

if __name__ == '__main__':
    print("🚀 NGO AI Backend Server Chal Raha Hai...")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)