from flask import Blueprint, request
from models.mongodb import Database

student_blueprint= Blueprint('student',__name__,url_prefix='/student')

@student_blueprint.route('/login',methods=['POST'])
def validate_student_login():
    username= request.form["username"]
    password= request.form["password"]
    Database.initialize()
    student = Database.find("student", {"username" : username})
    if(student is not None and student.password == password):
        return student
    else:
        Database.close()
        return False

@student_blueprint.route('/addcourse/<student_username>/<course_id>')
def add_course(student_username, course_id):
    result = Database.update("Student", {"username": student_username}, {'$push': {'course_list': course_id}} )
    return result.acknowledged

@student_blueprint.route('/removecourse/<student_username>/<course_id>')
def remove_course(student_username, course_id):
    result= Database.update("Student", {"username": student_username}, {'$pull': {'course_list': course_id}})
    return result.acknowledged

@student_blueprint.route('/update_student/<username>',methods=['POST'])
def update_student(username):
    new_values=request.json
    result= Database.update("Student",{"username":username}, {"$set": new_values})
    return result.acknowledged
