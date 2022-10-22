from flask import Blueprint, request, jsonify
from models.mongodb import Database
from bson.json_util import dumps, loads,ObjectId
import re
course_blueprint= Blueprint('course',__name__,url_prefix='/course')

@course_blueprint.route('/getall')
def get_all_courses():
    Database.initialize()
    result = Database.find("Course")
    if(result is not None):
        return loads(dumps(result))
    else:
        return[]

@course_blueprint.route('/getid/<course_id>')
def get_course(course_id):
    course = Database.find_single("Course", {"_id":ObjectId(course_id)})
    return loads(dumps(course))

def get_course_section(course_id):
    return get_course(course_id)['sections']

def get_courses(courses_id):
    Database.initialize()
    courses = Database.find("Course", {"_id":{ "$in": [ObjectId(id) for id in courses_id] }})
    return loads(dumps(courses))

@course_blueprint.route('/getname/<search>')
def search_course(search):
    Database.initialize()
    result = Database.find("Course", {"name":re.compile(search, re.IGNORECASE)})
    return dumps(result)

def add_course(data):
    json=loads(data)
    if(Database.count("Course",{"id":json['courseID']})==0):
        result=Database.insert_one("Course",data)
        return result.inserted_id
    else:
        return False

@course_blueprint.route('/update/<course_id>',methods=['POST'])
def update_course(course_id):
    request_data=request.json
    result= Database.update("Course", {"id":course_id}, {"$set": request_data})
    return result.acknowledged

def update_remove_waitlist(courseId):
    course_waitlist = Database.find_single("Course", {"_id": ObjectId(courseId)})['waitlist.count']
    if(course_waitlist>0):
        Database.update("Course", {"_id": ObjectId(courseId)}, {'$inc': {"waitlist.count":-1}})
        student= Database.find_single("Course",{"_id":ObjectId(courseId)})["waitlist.list"][0]
        add_waitlisted_course(student,courseId)

def add_waitlisted_course(student_username, course_id):
    Database.initialize()
    Database.update("Student", {"username": student_username}, {'$push': {'courses': ObjectId(course_id)}} )
    return "Course has been added"

def update_add_waitlist(courseId, studentId):
    Database.update("Course", {"_id": ObjectId(courseId)}, {'$inc': {"waitlist.count":1}})
    Database.update("Course", {"_id": ObjectId(courseId)}, {'$push': {'waitlist.list': ObjectId(studentId)}})
    return "Waitlist Added!"

def delete_course(courseId):
    remove_all_student_course(courseId, get_course(courseId))
    Database.delete("Course", {"_id":ObjectId(courseId)})

def remove_all_student_course(course_id, courses):
    Database.initialize()
    students= loads(courses)['student']
    for student in students:
        Database.update("Student", {"_id": ObjectId(student)}, {'$pull': {'courses': ObjectId(course_id)}})

def add_student(studentId, courseId):
    course= loads(get_course(courseId))
    capacity=course['capacity']
    counts=len(course['student'])
    if(counts>capacity):
        update_add_waitlist(courseId, studentId)
        return False
    else:
        Database.update("Course", {"_id": ObjectId(courseId)}, {'$push': {'student': ObjectId(studentId)}})
        return True

def remove_student(studentId, courseId):
    Database.update("Course", {"_id": ObjectId(courseId)}, {'$pull': {'student': ObjectId(studentId)}})
    update_remove_waitlist(courseId)
