from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generates a secure random key

def init_db():
    conn = sqlite3.connect('reso.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            payment_amount REAL NOT NULL,
            with_gst BOOLEAN NOT NULL,
            total_payable_amount REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        payment_amount = float(request.form['payment_amount'])
        with_gst = request.form.get('gst_option') == 'with_gst'
        
        # Calculate total payable amount
        if with_gst:
            total_payable_amount = payment_amount + (payment_amount * 0.18)
        else:
            total_payable_amount = payment_amount

        # Save to database
        conn = sqlite3.connect('reso.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO payments (name, payment_amount, with_gst, total_payable_amount)
            VALUES (?, ?, ?, ?)
        ''', (name, payment_amount, with_gst, total_payable_amount))
        conn.commit()
        conn.close()

        flash('Payment details submitted successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)