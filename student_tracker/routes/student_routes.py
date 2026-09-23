from flask import Blueprint, request, jsonify

from services.student_service import (
    create_student,
    get_all_students,
    add_assignment,
    get_top_performers,
    get_average_score
)

from database.db import students_collection

student_bp = Blueprint("student_bp", __name__)


# API 1: Add Student
@student_bp.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")

    if not name or not email or not course:
        return jsonify({
            "message": "All fields are required"
        }), 400

    existing = students_collection.find_one(
        {"email": email}
    )

    if existing:
        return jsonify({
            "message": "Email already exists"
        }), 400

    student_id = create_student(data)

    return jsonify({
        "message": "Student added",
        "student_id": student_id
    }), 201


# API 2: Get All Students
@student_bp.route("/students", methods=["GET"])
def get_students():

    students = get_all_students()

    return jsonify(students), 200

@student_bp.route(
    "/students/<student_id>/assignments",
    methods=["POST"]
)
def create_assignment(student_id):

    data = request.get_json()

    title = data.get("title")
    score = data.get("score")

    if not title:
        return jsonify({
            "message": "Title is required"
        }), 400

    if score is None:
        return jsonify({
            "message": "Score is required"
        }), 400

    if score < 0 or score > 100:
        return jsonify({
            "message": "Score must be between 0 and 100"
        }), 400

    assignment = {
        "title": title,
        "score": score
    }

    add_assignment(student_id, assignment)

    return jsonify({
        "message": "Assignment added successfully"
    }), 200


@student_bp.route(
    "/students/top-performers/<int:score>",
    methods=["GET"]
)
def top_performers(score):

    students = get_top_performers(score)

    return jsonify(students), 200


@student_bp.route(
    "/students/<student_id>/average",
    methods=["GET"]
)
def average_score(student_id):

    result = get_average_score(student_id)

    if result is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify(result), 200