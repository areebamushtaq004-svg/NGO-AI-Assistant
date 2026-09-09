from flask import Flask
from flask_cors import CORS
from database import init_db
from routes import chat, donation, faq, volunteer

app = Flask(__name__)
CORS(app)

# Database initialize karo
init_db()

# Sabhi routes (APIs) ko app ke sath joro (Blueprints)
app.register_blueprint(chat.chat_bp)
app.register_blueprint(donation.donation_bp)
app.register_blueprint(faq.faq_bp)
app.register_blueprint(volunteer.volunteer_bp)

if __name__ == '__main__':
    print("🚀 NGO AI Backend Server Chal Raha Hai...")
    app.run(debug=True, port=5000)