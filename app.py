from flask import Flask, send_from_directory
from flask_cors import CORS
from database import init_db, get_db
from routes import chat, donation, faq, volunteer, contact  # <--- Yahan 'contact' hona zaroori hai

app = Flask(__name__, static_folder='frontend')
CORS(app)

# Register Blueprints
app.register_blueprint(chat.chat_bp)
app.register_blueprint(donation.donation_bp)
app.register_blueprint(faq.faq_bp)
app.register_blueprint(volunteer.volunteer_bp)
app.register_blueprint(contact.contact_bp)  # <--- Yeh line zaroor honi chahiye

# (Yahan aapka admin-view wala code bhi ho sakta hai, usay mat chherein)

if __name__ == '__main__':
    init_db()
    print("🚀 NGO AI Backend Server Chal Raha Hai...")
    app.run(debug=True)