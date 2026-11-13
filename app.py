
from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {
        "id": 101,
        "name": "Arun Kumar",
        "department": "Information Technology",
        "year": 2
    },
    {
        "id": 102,
        "name": "Priya Sharma",
        "department": "Computer Science",
        "year": 2
    },
    {
        "id": 103,
        "name": "Rahul",
        "department": "Information Technology",
        "year": 3
    }
]


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>University Student Information System</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eef4ff;
                text-align: center;
                padding: 50px;
            }
            .card {
                background: white;
                padding: 35px;
                border-radius: 12px;
                max-width: 650px;
                margin: auto;
                box-shadow: 0 3px 12px #ccd5e3;
            }
            h1 {
                color: #2456a6;
            }
            a {
                display: inline-block;
                margin: 10px;
                padding: 12px 20px;
                background: #2456a6;
                color: white;
                text-decoration: none;
                border-radius: 6px;
            }
            a:hover {
                background: #173d7a;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>University Student Information System</h1>
            <p>Cloud-Based University Management System</p>
            <p>Welcome to the Student Information Portal.</p>
            <a href="/api/students">View Student Records</a>
            <a href="/health">Check API Status</a>
        </div>
    </body>
    </html>
    """


@app.route("/api/students")
def get_students():
    return jsonify({
        "status": "success",
        "total_students": len(students),
        "students": students
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "University Student Information System"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
