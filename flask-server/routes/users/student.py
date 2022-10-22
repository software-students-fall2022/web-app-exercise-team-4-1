from flask import Blueprint, request
from models.mongodb import Database
from bson.json_util import dumps, loads, ObjectId
from ..course import remove_student, add_student, get_courses
student_blueprint= Blueprint('student',__name__,url_prefix='/student')

def get_student_oid(username):
    return Database.find_single("Student", {"username": username})['_id']

def get_student_courses(username):
    courses= Database.find_single("Student", {"username": username})['course_list']
    return get_courses(courses)

@student_blueprint.route('/addcourse/<student_username>', methods=['GET','POST'])
def add_course(student_username):
    Database.initialize()
    course_id = request.form["course_id"]
    course_count= Database.count("Student",{"username": student_username, "courses":{"$in":[ObjectId(course_id)]}})
    if(course_count == 0):
        if(add_student(get_student_oid(student_username), course_id)):
            Database.update("Student", {"username": student_username}, {'$push': {'courses': ObjectId(course_id)}} )
            return "Course has been added"
        else:
            return "Class added to waitlist"
    else:
        return "Class is already enrolled"


@student_blueprint.route('/removecourse/<student_username>', methods=['GET','POST'])
def remove_course(student_username):
    Database.initialize()
    course_id = request.form["course_id"]
    student= Database.update("Student", {"username": student_username}, {'$pull': {'courses': ObjectId(course_id)}})
    remove_student(student.upserted_id, course_id)
    return "Class has been removed"

@student_blueprint.route('/update_student/<username>',methods=['POST'])
def update_student(username):
    Database.initialize()
    new_values=request.form
    Database.update("Student",{"username":username}, {"$set": new_values})
    return "Update is complete!"

@student_blueprint.route('/get_cart/<username>')
def get_cart(username):
    Database.initialize()
    cart= list(Database.find_single("Student",{"username":username},{'_id':0,'Carts':1})['Carts'])
    return get_courses(cart)

@student_blueprint.route('/add_all_cart/<username>')
def add_all_cart(username):
    Database.initialize()
    json = loads(get_cart(username))
    for course in json:
        add_student(get_student_oid(username), course['_id'])

