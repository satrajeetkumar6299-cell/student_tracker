from flask import Flask
from routes.student_routes import student_bp

app = Flask(__name__)

app.register_blueprint(student_bp)

if __name__ == "__main__":
    app.run(debug=True)