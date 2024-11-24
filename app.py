from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

# Database connection setup
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=EDONLUSJANI\SQLEXPRESS;'
        'DATABASE=TicSys;'
        'UID=edon.lusjani;'
        'PWD=Ed23082003$'  # Replace these with your actual credentials
    )
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit-reservation', methods=['POST'])
def submit_reservation():
    try:
        data = request.get_json()
        name = data['name']
        date = data['date']
        time = data['time']
        selected_pcs = data['selected_pcs']

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the reservation into the database
        cursor.execute("""
            INSERT INTO reservations (name, reservation_date, reservation_time, selected_pcs)
            VALUES (?, ?, ?, ?)
        """, (name, date, time, selected_pcs))

        conn.commit()
        conn.close()

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
