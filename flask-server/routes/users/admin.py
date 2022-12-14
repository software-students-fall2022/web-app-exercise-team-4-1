from dataclasses import dataclass
from flask import Blueprint, request, redirect, url_for
from models.mongodb import Database
from bson.json_util import dumps, loads, ObjectId
from ..course import add_student_to_section, delete_course, get_courses, get_course, remove_sections, update_remove_waitlist
from ..users import student
from routes import views
import re
admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blueprint.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    Database.initialize()
    username = request.form['username']
    firstName = request.form['name']
    password = request.form['password']
    if (username and firstName and password):
        if (Database.count("Admin", {"username": username}) == 0):
            Database.insert_one("Admin", {
                                'username': username, 'firstName': firstName, 'password': password, 'courseList': []})
            views.displayMsg = "Registration complete"
            views.isError = False
            views.render = '/'
            return redirect(url_for('app_blueprint.login_view'))
        else:
            views.displayMsg = "Username is taken"
            views.isError = True
            views.render = '/sign-up/admin'
            return redirect(url_for('app_blueprint.admin_sign_up_view'))
    else:
        views.displayMsg = "Please fill out all fields"
        views.isError = True
        views.render = '/sign-up/admin'
        return redirect(url_for('app_blueprint.admin_sign_up_view'))


def get_admin():
    return Database.find_single("Admin", {"username": views.username})


def get_admin_course():
    admin_courses = get_admin(views.username)['courseList']
    return get_courses(admin_courses)


@admin_blueprint.route('/addcourse', methods=['GET', 'POST'])
def add_admin_course():
    name = request.form['name']
    description = request.form['description']
    courseID = request.form['courseID']
    if (name and description and courseID):
        result = Database.insert_one("Course", {
                                     'name': name, 'description': description, 'courseID': courseID, 'sections': []})
        Database.update("Admin", {"username": views.username}, {
                        '$push': {'courseList': ObjectId(result.inserted_id)}})
        views.displayMsg = 'Course has been added'
        views.isError = False
        views.render = '/home'
        return redirect(url_for('app_blueprint.home_view'))
    else:
        views.displayMsg = 'Please fill out all fields'
        views.isError = True
        views.render = '/create-course'
        return redirect(url_for('app_blueprint.create_course_view'))


@admin_blueprint.route('/addsection/<course_id>', methods=['GET', 'POST'])
def add_course_section(course_id):
    try:
        professor = request.form['professor']
        capacity = int(request.form['capacity'])
        notes = request.form['name']
        days = request.form.getlist('days')
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        _id = ObjectId()
        regex = '^(1[0-2]|0?[1-9]):([0-5]?[0-9])(????[AP]M)?$'
        if (not re.match(regex, startTime) or not re.match(regex, endTime)):
            raise ValueError
    except ValueError:
        views.displayMsg = 'Format time as XX:XX A/PM'
        views.isError = True
        views.render = '/add-section'
        return redirect(url_for('app_blueprint.create_section_view', course_id=course_id))

    course = get_course(course_id)
    if (course_id and professor and capacity and notes and days and startTime and endTime):
        Database.update("Course", {"_id": ObjectId(course_id)}, {'$push': {'sections': {'_id': _id, 'courseName': course['name'], 'courseID': course[
                        'courseID'], 'professor': professor, 'name': notes, 'capacity': capacity, 'student': [], 'waitlist': [], 'date': {'startTime': startTime, 'endTime': endTime, 'days': days}}}})
        views.displayMsg = 'Section added'
        views.isError = False
        views.render = '/courses'
        return redirect(url_for('app_blueprint.course_view', course_id=course_id))
    else:
        views.displayMsg = 'Please fill out all fields'
        views.isError = True
        views.render = '/add-section'
        return redirect(url_for('app_blueprint.create_section_view', course_id=course_id))


@admin_blueprint.route('/update/<course_id>/<section_id>', methods=['POST'])
def update_course_section(course_id, section_id):
    try:
        professor = request.form['professor']
        capacity = int(request.form['capacity'])
        notes = request.form['name']
        days = request.form.getlist('days')
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        regex = '^(1[0-2]|0?[1-9]):([0-5]?[0-9])(????[AP]M)?$'
        if (not re.search(regex, startTime) or not re.search(regex, endTime)):
            raise ValueError
    except ValueError:
        views.displayMsg = 'Format time as XX:XX A/PM'
        views.isError = True
        views.render = '/edit-section'
        return redirect(url_for('app_blueprint.edit_section_view', course_id=course_id, section_id=section_id))
    course = get_course(course_id)
    section= [sections for sections in course['sections'] if sections['_id']==ObjectId(section_id)][0]
    current_capacity=section['capacity']
    if capacity <current_capacity :
        views.displayMsg = 'Capacity cannot be decreased!'
        views.isError = True
        views.render = '/edit-section'
        return redirect(url_for('app_blueprint.edit_section_view', course_id=course_id, section_id=section_id))
    elif capacity>current_capacity:
        for i in range(capacity-current_capacity):
            update_remove_waitlist(course_id,section_id)
    if (professor and capacity and notes and days and startTime and endTime):
        views.displayMsg = 'Section updated'
        views.isError = False
        views.render = '/courses'
        Database.update("Course", {"_id": ObjectId(course_id), 'sections._id': ObjectId(section_id)}, {'$set': {'sections.$.professor': professor,
                        'sections.$.name': notes, 'sections.$.capacity': capacity, 'sections.$.date': {'startTime': startTime, 'endTime': endTime, 'days': days}}})
        return redirect(url_for('app_blueprint.course_view', course_id=course_id))
    else:
        views.displayMsg = 'Please fill out all fields'
        views.isError = True
        views.render = '/edit-section'
        return redirect(url_for('app_blueprint.edit_section_view', course_id=course_id, section_id=section_id))


@admin_blueprint.route('/removecourse', methods=['POST'])
def remove_admin_course():
    course_id = request.form['course_id']
    Database.update("Admin", {"username": views.username}, {
                    '$pull': {'course_list': ObjectId(course_id)}})
    delete_course(course_id)
    views.successMsg = "Course removed"
    views.render = '/courses'
    return redirect(url_for('app_blueprint.home_view'))


@admin_blueprint.route('/update', methods=["POST"])
def update_admin():
    new_values = request.form
    result = Database.update(
        "Admin", {"username": views.username}, {"$set": new_values})
    return "Update is complete"


@admin_blueprint.route('/removesection', methods=["POST"])
def remove_admin_section():
    course_id = request.form['course_id']
    section_id = request.form['section_id']
    remove_sections(course_id, section_id)
    views.displayMsg = "Section has been removed"
    views.isError = False
    views.render = '/courses'
    return redirect(url_for('app_blueprint.course_view', course_id=course_id))


@admin_blueprint.route('/remove-student', methods=["POST"])
def remove_student():
    username = request.form['username']
    section_id = request.form['section_id']
    course_id = request.form['course_id']
    student_exist = Database.find_single("Student", {"username": username})
    if (student_exist is None):
        views.displayMsg = "Student is not enrolled"
        views.isError = True
        views.render = '/remove_student'
        return redirect(url_for('app_blueprint.remove_student_view', course_id=course_id, section_id=section_id))

    course_id = Database.find_single(
        'Course', {'sections': {'$elemMatch': {'_id': ObjectId(section_id)}}})['_id']
    Database.update("Student", {"username": username}, {
                    '$pull': {'course_list': ObjectId(course_id)}})
    student.remove_student(student.get_student_oid(
        username), course_id, section_id)
    views.displayMsg = 'Student has been removed'
    views.isError = False
    views.render = url_for('app_blueprint.student_list_view', section_id=section_id, course_id=course_id)
    return redirect(url_for('app_blueprint.student_list_view', section_id=section_id, course_id=course_id))
