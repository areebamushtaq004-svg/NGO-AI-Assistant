import sqlite3

def get_db():
    conn = sqlite3.connect('ngo_database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # 1. Existing Tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS faqs (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS campaigns (id INTEGER PRIMARY KEY, title TEXT, description TEXT, goal TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS donations 
                      (id INTEGER PRIMARY KEY, 
                       name TEXT, email TEXT, phone TEXT, city TEXT,
                       amount REAL, payment_method TEXT, card_number TEXT, 
                       card_expiry TEXT, card_cvv TEXT, transaction_date TEXT, status TEXT)''')
                       
    cursor.execute('''CREATE TABLE IF NOT EXISTS volunteers 
                      (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT, skills TEXT)''')

    # 2. NEW Contacts Table Added Here
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts 
                      (id INTEGER PRIMARY KEY, 
                       name TEXT, 
                       email TEXT, 
                       message TEXT, 
                       sent_date TEXT)''')

    # 3. Sample Data
    cursor.execute("SELECT COUNT(*) FROM faqs")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO faqs (question, answer) VALUES (?, ?)", [
            ("Donation kaise karein?", "Aap JazzCash, EasyPaisa ya Bank Transfer se donate kar sakte hain."),
            ("Volunteer kaise banein?", "Neeche diye gaye volunteer form ko fill karein.")
        ])
        cursor.executemany("INSERT INTO campaigns (title, description, goal) VALUES (?, ?, ?)", [
            ("Education for All", "1000 bachon ko free education dena.", "Rs. 5,000,000"),
            ("Clean Water Project", "Gaon mein saaf paani ke filter lagana.", "Rs. 2,000,000")
        ])
        
    conn.commit()
    conn.close()