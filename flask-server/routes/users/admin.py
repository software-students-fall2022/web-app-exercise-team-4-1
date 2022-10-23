from dataclasses import dataclass
from flask import Blueprint, request,redirect,url_for
from models.mongodb import Database
from bson.json_util import dumps, loads, ObjectId
from ..course import add_course, delete_course, get_courses, get_course
from routes import views
import re
admin_blueprint= Blueprint('admin',__name__,url_prefix='/admin')

@admin_blueprint.route('/sign_up', methods=['GET','POST'])
def sign_up():
    Database.initialize()
    username=request.form['username']
    firstName=request.form['name']
    password=request.form['password']
    if (username and firstName and password):
        if(Database.count("Admin",{"username":username})==0):
            Database.insert_one("Admin", {'username': username,'firstName': firstName, 'password':password, 'courseList':[]})
            views.displayMsg="Reigstration Complete!"
            views.isError= False
            views.render='/'
            return redirect(url_for('app_blueprint.login_view'))
        else:
            views.displayMsg="Username is taken!"
            views.isError= True
            views.render='/sign-up/admin'
            return redirect(url_for('app_blueprint.admin_sign_up_view'))
    else:
        views.displayMsg="Please fill up all fields!"
        views.isError= True
        views.render='/sign-up/admin'
        return redirect(url_for('app_blueprint.admin_sign_up_view'))

def get_admin():
    return Database.find_single("Admin", {"username": views.username})

def get_admin_course():
    admin_courses= get_admin(views.username)['courseList']
    return get_courses(admin_courses)

@admin_blueprint.route('/addcourse', methods = ['GET','POST'])
def add_admin_course():
    name=request.form['name']
    description=request.form['description']
    courseID=request.form['courseID']
    if(name and description and courseID):  
        result = Database.insert_one("Course", {'name':name,'description':description,'courseID':courseID,'sections':[]})
        Database.update("Admin", {"username": views.username}, {'$push': {'courseList': ObjectId(result.inserted_id)}})
        views.displayMsg='Course has been added!'
        views.isError= False
        views.render='/home'
        return redirect(url_for('app_blueprint.home_view'))
    else:
        views.displayMsg='Please complete all fields!'
        views.isError = True
        views.render='/create-course'
        return redirect(url_for('app_blueprint.create_course_view'))


@admin_blueprint.route('/addsection/<course_id>', methods = ['GET','POST'])
def add_course_section(course_id):
    try:
        professor= request.form['professor']
        capacity= int(request.form['capacity'])
        notes=request.form['notes']
        days=request.form.getlist('days')
        startTime=request.form['startTime']
        endTime=request.form['endTime']
        _id=ObjectId()
        regex = '^(1[0-2]|0?[1-9]):([0-5]?[0-9])(●?[AP]M)?$'
        if(not re.match(regex,startTime) or not re.match(regex, endTime)):
            raise ValueError
    except ValueError:
        views.displayMsg='Wrong format!'
        views.isError = True
        views.render='/add-section'
        return redirect(url_for('app_blueprint.create_section_view',course_id=course_id))

    course= get_course(course_id)
    if(course_id and professor and capacity and notes and days and startTime and endTime):
        Database.update("Course", {"_id": ObjectId(course_id)}, {'$push': {'sections': {'_id': _id,'courseName':course['name'], 'courseID':course['courseID'], 'professor': professor, 'name':notes, 'capacity':capacity, 'student':[],'waitlist':[],'date':{'startTime':startTime,'endTime':endTime,'days':days}}}})
        views.displayMsg='Section Added!'
        views.isError= False
        views.render='/courses'
        return redirect(url_for('app_blueprint.course_view',course_id=course_id))
    else:
        views.displayMsg='Please complete all fields!'
        views.isError = True
        views.render='/add-section'      
        return redirect(url_for('app_blueprint.create_section_view',course_id=course_id))

@admin_blueprint.route('/update/<course_id>/<section_id>',methods=['POST'])
def update_course_section(course_id,section_id):
    try:
        professor= request.form['professor']
        capacity= int(request.form['capacity'])
        notes="test" #request.form['notes']
        days=request.form.getlist('days')
        startTime=request.form['startTime']
        endTime=request.form['endTime']
        regex = '^(1[0-2]|0?[1-9]):([0-5]?[0-9])(●?[AP]M)?$'
        if(not re.search(regex,startTime) or not re.search(regex, endTime)):
            raise ValueError
    except ValueError:
        views.displayMsg='Wrong format!'
        views.isError = True
        views.render='/edit-section'
        return redirect(url_for('app_blueprint.edit_section_view',course_id=course_id,section_id=section_id))

    if(professor and capacity and notes and days and startTime and endTime):
        views.displayMsg='Section updated!'
        views.isError= False
        views.render='/courses'
        Database.update("Course", {"_id": ObjectId(course_id), 'sections._id': ObjectId(section_id)}, {'$set': {'sections.$.professor': professor, 'sections.$.name':notes, 'sections.$.capacity':capacity,'sections.$.date':{'startTime':startTime,'endTime':endTime,'days':days}}})
        return redirect(url_for('app_blueprint.course_view',course_id=course_id))
    else:
        views.displayMsg='Please complete all fields!'
        views.isError = True
        views.render='/edit-section'
        return redirect(url_for('app_blueprint.edit_section_view',course_id=course_id,section_id=section_id))


@admin_blueprint.route('/removecourse', methods=['POST'])
def remove_admin_course():
    course_id= request.form['course_id']
    Database.update("Admin", {"username": views.username}, {'$pull': {'course_list': ObjectId(course_id)}})
    delete_course(course_id)
    views.successMsg="Course Removed!"
    views.render= '/courses'
    return redirect(url_for('app_blueprint.course_view'))

@admin_blueprint.route('/update',methods=["POST"])
def update_admin():
    new_values= request.form
    result= Database.update("Admin", {"username":views.username}, {"$set": new_values})
    return "Update is complete!"