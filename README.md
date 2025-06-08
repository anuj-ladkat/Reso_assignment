# Payment Details Application

A Flask-based web application that allows users to enter payment details and store them in an SQLite database.

## Features

- User-friendly form for entering payment details
- GST calculation (18%) option
- Real-time total amount calculation
- Responsive design using Bootstrap
- SQLite database storage

## Setup Instructions

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py or python3 app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Database

The application uses SQLite with the following schema:
- Database name: `reso.db`
- Table name: `payments`
- Fields:
  - id (INTEGER, PRIMARY KEY)
  - name (TEXT)
  - payment_amount (REAL)
  - with_gst (BOOLEAN)
  - total_payable_amount (REAL)
  - created_at (TIMESTAMP)

## Technologies Used

- Flask
- SQLite
- Bootstrap 5
- Jinja2
- HTML/CSS/JavaScript
