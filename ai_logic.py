def detect_language(msg):
    urdu_markers = ['kaise', 'kasay', 'karna', 'karo', 'dena', 'lo', 'chahta', 'chahti', 
                    'mujhe', 'mera', 'apna', 'kya', 'hai', 'hain', 'batao', 'tarika']
    for word in urdu_markers:
        if word in msg:
            return 'urdu'
    return 'english'

def get_ai_response(user_message):
    msg = user_message.lower().strip()
    lang = detect_language(msg)
    res = {"text": "", "button": None}
    
    if lang == 'urdu':
        # --- VOLUNTEER (Urdu) ---
        if any(k in msg for k in ['volunteer', 'shamil', 'join', 'member', 'madadgar']):
            res["text"] = "Volunteer banne ke liye barah-e-karam neeche diye gaye button par click karke form fill karein. Aapka shukriya!"
            res["button"] = {"text": "📝 Volunteer Form Fill Karein", "url": "forms.html#volunteer-section"}
            
        # --- CONTACT (Urdu) ---
        elif any(k in msg for k in ['contact', 'rabta', 'number', 'phone', 'email', 'message']):
            res["text"] = "Aap humse rabta karne ke liye neeche diye gaye button par click karein aur apna message bhejein."
            res["button"] = {"text": "📩 Contact Form Kholein", "url": "forms.html#contact-section"}
            
        # --- CAMPAIGNS (Urdu) - (Yeh wapis add kiya hai) ---
        elif any(k in msg for k in ['campaign', 'muhim', 'project', 'kaam', 'yोजना']):
            res["text"] = "Hamari mojooda muhimat: 1) 'Education for All' (1000 bachon ko taleem) 2) 'Clean Water Project' (saaf pani). Aap in mein shamil ho sakte hain!"
            
        # --- DONATION (Urdu) ---
        elif any(k in msg for k in ['donat', 'chanda', 'paisa', 'madad']):
            res["text"] = "Aap JazzCash (0300-1234567) ya Bank Account (HBL 1234-5678) ke zariye donation kar sakte hain. Allah aapko jazaye khair de!"
            
        # --- GREETING (Urdu) ---
        elif any(k in msg for k in ['salam', 'aoa', 'adaab', 'khair']):
            res["text"] = "وعلیکم السلام! 🌟 Main NGO AI Assistant hoon. Aap mujhse Donation, Volunteer, ya Contact ke baray mein puch sakte hain."
            
    else: # --- ENGLISH ---
        # --- VOLUNTEER (English) ---
        if any(k in msg for k in ['volunteer', 'join', 'help', 'member']):
            res["text"] = "To become a volunteer, please click the button below to fill out the registration form. Thank you!"
            res["button"] = {"text": "📝 Open Volunteer Form", "url": "forms.html#volunteer-section"}
            
        # --- CONTACT (English) ---
        elif any(k in msg for k in ['contact', 'phone', 'email', 'reach', 'number', 'message']):
            res["text"] = "You can reach out to us by clicking the button below and sending us a message."
            res["button"] = {"text": "📩 Open Contact Form", "url": "forms.html#contact-section"}
            
        # --- CAMPAIGNS (English) - (Yeh wapis add kiya hai) ---
        elif any(k in msg for k in ['campaign', 'project', 'initiative', 'cause']):
            res["text"] = "Our current campaigns: 1) 'Education for All' (educating 1000 children) 2) 'Clean Water Project'. Join us in making a difference!"
            
        # --- DONATION (English) ---
        elif any(k in msg for k in ['donat', 'money', 'fund', 'contribute']):
            res["text"] = "You can donate via JazzCash (0300-1234567) or Bank Account (HBL 1234-5678). Every contribution makes a difference!"
            
        # --- GREETING (English) ---
        elif any(k in msg for k in ['hello', 'hi', 'hey', 'good']):
            res["text"] = "Hello! 👋 I'm the NGO AI Assistant. You can ask me about Donations, Volunteering, or Contact info."

    # Fallback
    if not res["text"]:
        res["text"] = "Maaf karein, main samajh nahi saka. 'help' type karein." if lang == 'urdu' else "I didn't understand. Please type 'help'."
        
    return res