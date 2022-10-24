from flask import Blueprint, request, jsonify, redirect,url_for
from models.mongodb import Database
from bson.json_util import dumps, loads,ObjectId
from routes import views
import re
course_blueprint= Blueprint('course',__name__,url_prefix='/course')

@course_blueprint.route('/getall')
def get_all_courses():
    result = Database.find("Course")
    if(result is not None):
        return loads(dumps(result))
    else:
        return[]

def get_all_students():
    result = Database.find("Student")
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
    courses = Database.find("Course", {"_id":{ "$in": [ObjectId(id) for id in courses_id] }})
    return loads(dumps(courses))

@course_blueprint.route('/getname/<search>')
def search_course(search):
    Database.initialize()
    result = Database.find("Course", {"name":re.compile(search, re.IGNORECASE)})
    return loads(dumps(result))

@course_blueprint.route('/addcourse', methods=['GET','POST'])
def add_student_to_section():
    section_id=request.form['section_id']
    course_id= Database.find_single('Course', {'sections': {'$elemMatch':{'_id': ObjectId(section_id)}}})['_id']
    if(views.admin):
        username=request.form['username']
        student_exist= Database.find_single("Student",{"username":username})
        if(student_exist is None):
            views.displayMsg= "Student does not exist"
            views.isError=True
            views.render='/add_student'
            return redirect(url_for('app_blueprint.add_student_view',course_id=course_id,section_id=section_id))
        course_count= Database.count("Student",{"username": username, "courses":{"$in":[ObjectId(course_id)]}})
        if(course_count == 0):
            student_oid= Database.find_single("Student", {"username": username})['_id']
            if(add_student(student_oid, course_id,section_id)):
                Database.update("Student", {"username": username}, {'$push': {'courses': ObjectId(course_id)}} )
                views.displayMsg= "Student has been added!"
                views.isError=False
                views.render='/add_student'
                return redirect(url_for('app_blueprint.add_student_view',course_id=course_id,section_id=section_id))
            else:
                views.displayMsg= 'Student in waitlist!'
                views.render='/add_student'
                return redirect(url_for('app_blueprint.add_student_view', course_id=course_id,section_id=section_id))
        else:
            views.displayMsg= 'Student is already enrolled!'
            views.isError=True
            views.render='/add_student'
            return redirect(url_for('app_blueprint.add_student_view',course_id=course_id,section_id=section_id))
    else:
        course_count= Database.count("Student",{"username": views.username, "course_list":{"$in":[ObjectId(course_id)]}})
        if(course_count == 0):
            student_oid= Database.find_single("Student", {"username": views.username})['_id']
            Database.update("Student", {"username": views.username}, {'$pull': {'carts': ObjectId(section_id)}} )
            if(add_student(student_oid,course_id,section_id)):
                Database.update("Student", {"username": views.username}, {'$push': {'course_list': ObjectId(course_id)}} )
                views.displayMsg= "Course has been added"
                views.isError=False
                views.render='/cart'
                return redirect(url_for('app_blueprint.shopping_cart_view'))

            else:
                views.displayMsg= "Course in waitlist!"
                views.isError=False
                views.render='/cart'
                return redirect(url_for('app_blueprint.shopping_cart_view'))
        else:
            views.displayMsg= "Course is already enrolled!"
            views.isError=True
            views.render='/cart'
            return redirect(url_for('app_blueprint.shopping_cart_view'))


@course_blueprint.route('/update/<course_id>',methods=['POST'])
def update_course(course_id):
    courseID= request.form['courseID']
    name= request.form['name']
    description= request.form['description']
    if(courseID and name and description):
        result= Database.update("Course", {"_id":ObjectId(course_id)}, {"$set": {'courseID': courseID, 'description':description,'name':name}})
        views.displayMsg= "Course has been updated!"
        views.isError= False
        views.render='/home'
        return redirect(url_for('app_blueprint.home_view'))
    else:
        views.displayMsg= "All fields must be filled!"
        views.isError = True
        views.render='/edit-course'
        return redirect(url_for('app_blueprint.edit_course_view', course_id=course_id)) 
    

def update_remove_waitlist(courseId, sectionId):
    course = get_course(courseId)
    section= [sections for sections in course['sections'] if sections['_id']==ObjectId(sectionId)][0]
    counts=len(section['waitlist'])    
    if(counts>0):
        student_id= section['waitlist'][0]
        add_waitlisted_course(student_id,courseId, sectionId)

def add_waitlisted_course(student_id, course_id, section_id):
    if Database.count("Student",{"_id": ObjectId(student_id), "course_list":{"$in":[ObjectId(course_id)]}}) ==0:
        Database.update("Course", {"_id": ObjectId(course_id), "sections._id": ObjectId(section_id)}, {'$pull': {'sections.$.waitlist': ObjectId(student_id)}})
        Database.update("Student", {"username": ObjectId(student_id)}, {'$push': {'course_list': ObjectId(course_id)}} )
        return True
    else:
        Database.update("Course", {"_id": ObjectId(course_id), "sections._id": ObjectId(section_id)}, {'$pull': {'sections.$.waitlist': ObjectId(student_id)}})
        return False

def update_add_waitlist(studentId,course_id, section_id):
    if Database.count("Course",{'sections': {'$elemMatch': {'_id': ObjectId(section_id), 'waitlist':ObjectId(studentId)}}})==0:
        Database.update("Course", {"_id": ObjectId(course_id), "sections._id": ObjectId(section_id)}, {'$push': {'sections.$.waitlist': ObjectId(studentId)}})
        return True
    else:
        return False

def delete_course(course_id):
    Database.delete("Course", {"_id":ObjectId(course_id)})
    students=list(get_all_students())
    student_ids= [ student['_id'] for student in students]
    for student in student_ids:
        Database.update("Student", {"_id": ObjectId(student)}, {'$pull': {'course_list': ObjectId(course_id)}})

def add_student(studentId, course_id, section_id):
    course = get_course(course_id)
    section= [sections for sections in course['sections'] if sections['_id']==ObjectId(section_id)][0]
    capacity=section['capacity']
    counts=len(section['student'])
    if(counts>=capacity):
        update_add_waitlist(studentId, course_id, section_id)
        return False
    else:
        Database.update("Course", {'_id':ObjectId(course_id), "sections._id": ObjectId(section_id)}, {'$push': {"sections.$.student": ObjectId(studentId)}})
        return True

def remove_student(studentId, courseId, sectionId):
    Database.update("Course", {'_id':ObjectId(courseId), "sections._id": ObjectId(sectionId)}, {'$pull': {"sections.$.student": ObjectId(studentId)}})
    update_remove_waitlist(courseId, sectionId)

def remove_sections(courseId, sectionId):
    Database.update("Course", {"_id": ObjectId(courseId)}, {'$pull': {'sections' : {'_id': ObjectId(sectionId)}}})

    students=list(get_all_students())
    student_ids= [ student['_id'] for student in students]
    for student in student_ids:
        Database.update("Student", {"_id": ObjectId(student)}, {'$pull': {'carts': ObjectId(sectionId)}})
        Database.update("Student", {"_id": ObjectId(student)}, {'$pull': {'course_list': ObjectId(courseId)}})
