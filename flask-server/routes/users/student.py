from flask import Blueprint
from extensions import mongo

student_blueprint= Blueprint("student", __name__, url_prefix='/student')

@student_blueprint.route('/get')
def get_student():
    student_collection = mongo.db.Student
    students= student_collection.find()
    return students

@student_blueprint.route('/add')
def add_student():
    student_collection = mongo.db.Student
    student_collection.insert_one()
    return "success"

@student_blueprint.route('/remove')
def remove_student():
    student_collection = mongo.db.Student
    student_collection.delete_one()
    return "success"

@student_blueprint.route('/update')
def update_student():
    student_collection = mongo.db.Student
    student_collection.update_one()
    return "success"