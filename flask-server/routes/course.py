from flask import Blueprint
from extensions import mongo

course_blueprint= Blueprint("course", __name__)

@course_blueprint.route('/course')
def get_course():
    course_collection = mongo.db.Course
    courses= course_collection.find()
    return courses

@course_blueprint.route('/add')
def add_course():
    courses_collection = mongo.db.Course
    courses_collection.insert_one()
    return "success"

@course_blueprint.route('/remove')
def remove_course():
    courses_collection = mongo.db.Course
    courses_collection.delete_one()
    return "success"

@course_blueprint.route('/update')
def update_course():
    courses_collection = mongo.db.Course
    courses_collection.update_one()
    return "success"