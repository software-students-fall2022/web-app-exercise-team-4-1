from dataclasses import dataclass
from flask import Blueprint, request
from models.mongodb import Database
from bson.json_util import dumps, loads, ObjectId
from ..course import add_course, delete_course, get_courses
from routes import views
admin_blueprint= Blueprint('admin',__name__,url_prefix='/admin')

def get_admin():
    return Database.find_single("Admin", {"username": views.username})

def get_admin_course():
    admin_courses= get_admin(views.username)['courseList']
    return get_courses(admin_courses)

@admin_blueprint.route('/addcourse', methods = ['GET','POST'])
def add_admin_course():
    new_values=request.form
    valid_id= add_course(dumps(new_values))
    if(valid_id):
        Database.insert("Admin", {"username": views.username}, {'$push': {'courseList': ObjectId(valid_id)}})
        return "Course Added!"
    else:
        return "Course ID already exists!"

@admin_blueprint.route('/addsection', methods = ['GET','POST'])
def add_course_section():
    course_id=request.form['course_id']
    professor= request.form['professor']
    capacity= request.form['capacity']
    notes=request.form['notes']
    days=request.form['days']
    startTime=request.form['startTime']
    endTime=request.form['endTime']

    Database.insert("Course", {"_id": course_id}, {'$push': {'sections': {'professor': professor, 'notes':notes, 'capacity':capacity, 'student':[],'waitlist':[],'date':{'startTime':startTime,'endTime':endTime,'days':days}}}})
    return "Section Added!"

@admin_blueprint.route('/removecourse/<course_id>')
def remove_admin_course(course_id):
    result= Database.update("Admin", {"username": views.username}, {'$pull': {'course_list': ObjectId(course_id)}})
    delete_course(course_id)
    return "Course Removed!"

@admin_blueprint.route('/update',methods=["POST"])
def update_admin():
    new_values= request.form
    result= Database.update("Admin", {"username":views.username}, {"$set": new_values})
    return "Update is complete!"