from flask import Blueprint
from extensions import mongo

course_blueprint= Blueprint("course", __name__)

@course_blueprint.route('/course/<mongoid>')
def get_course():
    course_collection = mongo.db.course
    courses= course_collection.find()
    return courses
    