from database.db import students_collection
from bson import ObjectId


def create_student(data):

    student = {
        "name": data["name"],
        "email": data["email"],
        "course": data["course"],
        "assignments": []
    }

    result = students_collection.insert_one(student)

    return str(result.inserted_id)


def get_all_students():

    students = []

    for student in students_collection.find():

        student["_id"] = str(student["_id"])

        students.append(student)

    return students


def add_assignment(student_id, assignment):

    result = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {
            "$push": {
                "assignments": assignment
            }
        }
    )

    return result.modified_count


def get_top_performers(score):

    students = []

    result = students_collection.find(
        {
            "assignments.score": {
                "$gte": score
            }
        }
    )

    for student in result:

        student["_id"] = str(student["_id"])

        students.append(student)

    return students


def get_average_score(student_id):

    student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if not student:
        return None

    assignments = student.get("assignments", [])

    if len(assignments) == 0:
        average = 0
    else:
        total = sum(a["score"] for a in assignments)
        average = total / len(assignments)

    return {
        "student": student["name"],
        "average_score": round(average, 2)
    }


def add_assignment(student_id, assignment):

    result = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {
            "$push": {
                "assignments": assignment
            }
        }
    )

    return result.modified_count


def get_top_performers(score):

    students = []

    result = students_collection.find(
        {
            "assignments.score": {
                "$gte": score
            }
        }
    )

    for student in result:

        student["_id"] = str(student["_id"])

        students.append(student)

    return students


def get_average_score(student_id):

    student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if not student:
        return None

    assignments = student.get("assignments", [])

    if len(assignments) == 0:
        average = 0
    else:
        total = sum(a["score"] for a in assignments)
        average = total / len(assignments)

    return {
        "student": student["name"],
        "average_score": round(average, 2)
    }