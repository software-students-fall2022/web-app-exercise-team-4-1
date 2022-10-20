from dataclasses import dataclass
from flask import Blueprint, request
from models.mongodb import Database
from bson.json_util import dumps, loads, ObjectId
from ..course import add_course, delete_course
admin_blueprint= Blueprint('admin',__name__,url_prefix='/admin')


@admin_blueprint.route('/login', methods=['POST'])
def validate_admin_login():
    username= request.form["username"]
    password= request.form["password"]
    Database.initialize()
    admin_count = Database.count("Admin", {"username" : username})
    if(admin_count==0):
        Database.close()
        return "Incorrect Username or Password"
    else:
        admin = Database.find("Admin", {"username" : username})
        if(admin.password == password):
            return dumps(admin)

@admin_blueprint.route('/addcourse/<username>', methods = ['GET','POST'])
def add_admin_course(admin_username):
    new_values=request.form
    valid_id= add_course(dumps(new_values))
    if(valid_id):
        Database.insert("Admin", {"username": admin_username}, {'$push': {'courseList': ObjectId(valid_id)}})
        return "Course Added!"
    else:
        return "Course ID already exists!"

@admin_blueprint.route('/removecourse/<admin_username>/<course_id>')
def remove_admin_course(admin_username, course_id):
    result= Database.update("Admin", {"username": admin_username}, {'$pull': {'course_list': ObjectId(course_id)}})
    delete_course(course_id)
    return "Course Removed!"

@admin_blueprint.route('/update',methods=["POST"])
def update_admin(username):
    new_values= request.form
    result= Database.update("Admin", {"username":username}, {"$set": new_values})
    return "Update is complete!"