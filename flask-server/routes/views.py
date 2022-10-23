from distutils.log import error
from flask import Blueprint, render_template, request, redirect, url_for
from .users.admin import get_admin_course
from .users.student import get_cart, get_student_courses, get_students, get_student_sections, get_student_waitlists
from .course import add_student, get_all_courses, get_course, get_course_section, search_course, remove_student
from bson.json_util import dumps, loads, ObjectId
from flask import Blueprint, render_template
import json

app_blueprint = Blueprint("app_blueprint", __name__)

admin = None
username = None
errorMsg = None
successMsg = None
render = None

def reset_message(render_page):
    if(render != render_page):
        global errorMsg
        errorMsg = None
        global successMsg
        successMsg=None

@app_blueprint.route('/')
def login_view():
    reset_message('/')
    return render_template('login_page.html', errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/sign-up')
def sign_up_view():
    reset_message('/sign-up')
    return render_template('sign_up.html', errorMsg=errorMsg, successMsg=successMsg)

@app_blueprint.route('/sign-up/admin')
def admin_sign_up_view():
    reset_message('/sign-up/admin')
    return render_template('admin_sign_up.html', errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/home')
def home_view():
    reset_message('/home')
    if admin:
        courses= search_course(request.args.get('searchterm', ""))
        return render_template('admin_courses.html', courses=courses, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)
    else:
        enrolled = get_student_sections()
        waitlist= get_student_waitlists()
        return render_template('student_courses.html', waitlist=waitlist, enrolled=enrolled, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>')
def course_view(course_id):
    reset_message('/courses')
    course = get_course(course_id)
    sections=course['sections']
    if admin:
        return render_template('admin_course.html', sections=sections, course=course, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)
    else:
        return render_template('course.html', sections=sections, course=course, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>/add-section')
def create_section_view(course_id):
    reset_message('/add-section')
    course = get_course(course_id)
    return render_template('create_section.html', course=course, admin=admin, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>/<section_id>/edit-section')
def edit_section_view(course_id, section_id):
    reset_message('/edit-section')
    course = get_course(course_id)
    section= [sections for sections in course['sections'] if sections['_id']==ObjectId(section_id)][0]
    return render_template('edit_section.html', course=course, admin=admin, section=section, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>/<section_id>/students')
def student_list_view(course_id, section_id):
    reset_message('courses/students')
    course= get_course(course_id)
    section = [section for section in course['sections'] if section['_id'] == ObjectId(section_id) ][0]
    docs= get_students(section['student'])
    return render_template('student_list.html', docs=docs, course=course, admin=admin, username=username, section=section, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>/<section_id>/students/add', methods=['GET', 'POST'])
def add_student_view(course_id, section_id):
    # course= get_course(course_id)
    # course_name=course['software engineering']
    # course_code=course['CS-474']
    # section_name=course['sections']['notes']

    if (request.method == 'POST'):
        studentId = request.form['studentId']
        add_student(studentId, course_id)
        return redirect(url_for('app_blueprint.student_list_view'))
    course = {"_id": 1, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
              "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"}
    section = {"_id": 12, 'professor': 'Amos Bloomberg', 'date': {'days': ['M', 'W'], 'startTime': '2:00PM', 'endTime': '3:15PM'}, 'capacity': 1, 'student': [ObjectId('635303beec3a435021103e89'), ObjectId(
        '635081d3c79712ba0de837cf')], 'waitlist': [ObjectId('6353040eec3a435021103e8a')], 'courseName': 'Software Engineering', 'courseID': 'CSCI-UA.474', '_id': ObjectId('635499bce6ec35919761b208'), 'name': 'Section 1'}
    return render_template('add_student.html', course=course, admin=admin, username=username, section=section, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>/<section_id>/students/remove', methods=['GET', 'POST'])
def remove_student_view(course_id, section_id):
    # course= get_course(course_id)
    # course_name=course['software engineering']
    # course_code=course['CS-474']
    # section_name=course['sections']['notes']
    if (request.method == 'POST'):
        studentId = request.form['studentId']
        remove_student(studentId, course_id)
        return redirect(url_for('app_blueprint.student_list_view'))

    course = {"_id": 1, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
              "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"}
    section = {"_id": 12, 'professor': 'Amos Bloomberg', 'date': {'days': ['M', 'W'], 'startTime': '2:00PM', 'endTime': '3:15PM'}, 'capacity': 1, 'student': [ObjectId('635303beec3a435021103e89'), ObjectId(
        '635081d3c79712ba0de837cf')], 'waitlist': [ObjectId('6353040eec3a435021103e8a')], 'courseName': 'Software Engineering', 'courseID': 'CSCI-UA.474', '_id': ObjectId('635499bce6ec35919761b208'), 'name': 'Section 1'}
    return render_template('remove_student.html', course=course, admin=admin, username=username, section=section, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses', methods=['GET'])
def course_search_view():
    courses= search_course(request.args.get('searchterm', ""))
    return render_template('course_search.html', courses=courses, admin=admin, username=username, successMsg=successMsg)


@app_blueprint.route('/cart')
def shopping_cart_view():
    sections= get_cart()
    return render_template('shopping_cart.html', sections=sections, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/create-course')
def create_course_view():
    reset_message('/create-course')
    return render_template('create_course.html', admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/edit-course/<course_id>')
def edit_course_view(course_id):
    reset_message('/edit-course')
    course=get_course(course_id)
    return render_template('edit_course.html', admin=admin, course=course, errorMsg=errorMsg, successMsg=successMsg)
