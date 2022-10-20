from flask import Blueprint, request, jsonify
from models.mongodb import Database
from bson.json_util import dumps, loads

course_blueprint= Blueprint('course',__name__,url_prefix='/course')

@course_blueprint.route('/getall')
def get_all_courses():
    courses = Database.find("Course")
    return courses

@course_blueprint.route('/get/<course_id>')
def get_course(course_id):
    course = Database.find_single("Course", {"id":course_id})
    if(course is not None):
        return course
    else:
        return "Course does not exists"

@course_blueprint.route('/add',methods=['POST'])
def add_course():
    request_data= request.form
    # You may need to convert the request_data into a JSON

    result=Database.insert_one("Course",request_data)
    return result.acknowledged

@course_blueprint.route('/remove',methods=['POST'])
def remove_course():
    request_data=request.json
    result=Database.delete("Course", {"id":request_data["id"]})

    return result.acknowledged

@course_blueprint.route('/update/<course_id>',methods=['POST'])
def update_course(course_id):
    request_data=request.json
    result= Database.update("Course", {"id":course_id}, {"$set": request_data})
    return result.acknowledged