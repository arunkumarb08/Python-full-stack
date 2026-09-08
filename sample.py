from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId   

app = Flask(__name__)


client = MongoClient("mongodb://localhost:27017")
db = client["mitsDB"]
students = db["students"]

@app.route("/students", methods=['POST'])
def add_student():
     # data = request.get_json()

    student = {
        'name': data['name'],
        'email': data['email'],
        'age': data['age']
    }

    result = students.insert_one(student)

    return jsonify({
        "message": "student created successfully"
    })

@app.route("/students", methods=['GET'])
def get_students():
    student_list = []
    for student in students.find():
        student_list.append({
            'name': student['name'],
            'email': student['email'],
            'age': student['age']
        })
    return jsonify(student_list)

@app.route("/students/<student_id>", methods=['GET'])
def get1_student(student_id):
    student = students.find_one({"_id": ObjectId(student_id)})
    if student:
        return jsonify({
            'name': student['name'],
            'email': student['email'],
            'age': student['age']
        })
    return jsonify({"message": "student not found"})




@app.route("/students/<student_id>", methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    result = students.update_one({"_id": ObjectId(student_id)}, {"$set": data})
    if result.modified_count == 1:
        return jsonify({"message": "student updated successfully"})
    return jsonify({"message": "student not found"})

@app.route("/students/<student_id>", methods=['DELETE'])
def delete_student(student_id):
    result = students.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count == 1:
        return jsonify({"message": "student deleted successfully"})
    return jsonify({"message": "student not found"})

if __name__ == "__main__":
    app.run(debug=True)
    