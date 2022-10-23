from flask import Blueprint, request, redirect, url_for
from models.mongodb import Database
from bson.json_util import dumps, loads, ObjectId
from ..course import get_all_courses, remove_student, add_student, get_courses
from routes import views
student_blueprint= Blueprint('student',__name__,url_prefix='/student')

def get_student_oid():
    return Database.find_single("Student", {"username": views.username})['_id']

def get_students(student_ids):
    courses = Database.find("Student", {"_id":{ "$in": [ObjectId(id) for id in student_ids] }})
    return loads(dumps(courses))

def get_student_courses():
    courses= Database.find_single("Student", {"username": views.username})['course_list']
    return get_courses(courses)

def get_student_sections():
    courses=get_student_courses()
    return get_sections(courses,ObjectId(get_student_oid()),'student')

def get_sections(courses, search, attribute):
    return([section for course in courses for section in course['sections'] if search in section[attribute]])

def get_student_waitlists():
    return get_sections(get_all_courses(),ObjectId(get_student_oid()),'waitlist')

@student_blueprint.route('/addcourse', methods=['GET','POST'])
def add_course():
    course_id = request.form["course_id"]

    course_count= Database.count("Student",{"username": views.username, "courses":{"$in":[ObjectId(course_id)]}})
    if(course_count == 0):
        if(add_student(get_student_oid(views.username), course_id)):
            Database.update("Student", {"username": views.username}, {'$push': {'courses': ObjectId(course_id)}} )
            return "Course has been added"
        else:
            return "Class added to waitlist"
    else:
        return "Class is already enrolled"


@student_blueprint.route('/removecourse', methods=['GET','POST'])
def remove_course():
    Database.initialize()
    course_id = request.form["course_id"]
    student= Database.update("Student", {"username": views.username}, {'$pull': {'courses': ObjectId(course_id)}})
    remove_student(student.upserted_id, course_id)
    return "Class has been removed"

@student_blueprint.route('/update_student',methods=['POST'])
def update_student():
    Database.initialize()
    new_values=request.form
    Database.update("Student",{"username":views.username}, {"$set": new_values})
    return "Update is complete!"

@student_blueprint.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    course_id = request.form["course_id"]
    Database.update("Student", {"username": views.username}, {'$push': {'Carts': ObjectId(course_id)}} )
    return redirect(url_for('app_blueprint.course_search_view'))

@student_blueprint.route('/get_cart')
def get_cart():
    carts= Database.find_single("Student",{"username":views.username},{'_id':0,'carts':1})['carts']
    courses= get_all_courses()
    return([section for course in courses for section in course['sections'] if section['_id'] in carts])

@student_blueprint.route('/add_all_cart')
def add_all_cart():
    Database.initialize()
    json = loads(get_cart(views.username))
    for course in json:
        add_student(get_student_oid(views.username), course['_id'])

