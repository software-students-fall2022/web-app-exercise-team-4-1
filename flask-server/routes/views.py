from distutils.log import error
from flask import Blueprint, render_template, request, redirect, url_for
from .users.admin import get_admin_course
from .users.student import get_cart, get_student_courses, get_students
from .course import add_student, get_all_courses, get_course, get_course_section, search_course, remove_student
from bson.json_util import dumps, loads, ObjectId
from flask import Blueprint, render_template
import json

app_blueprint = Blueprint("app_blueprint", __name__)

admin = None
username = None
errorMsg = None
successMsg = None


@app_blueprint.route('/')
def login_view():
    return render_template('login_page.html', errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/sign-up')
def sign_up_view():
    return render_template('sign_up.html', errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/home')
def home_view():
    if admin:
        courses= search_course(request.args.get('searchterm', ""))
        return render_template('admin_courses.html', courses=courses, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)
    else:
        enrolled = get_student_courses()
        waitlist = [
                {"_id": 32, "waitlistPosition": 1, "name":"001", "professor": "Professor X", "capacity": 1, "notes": "This is a section", "days": ["Mo", "We"], "startTime": "9:30AM", "endTime": "10:45AM", "students": [1,2], "courseID": "CSCI-UA.0001", "courseName": 'Intro to Computer Science'},
                {"_id": 32, "waitlistPosition": 2, "name":"002", "professor": "Professor X", "capacity": 30, "notes": "This is a section", "days": ["Mo", "We"], "startTime": "9:30AM", "endTime": "10:45AM", "courseID": "CSCI-UA.0002", "courseName": 'Intro to Birds'}
            ]
        return render_template('student_courses.html', waitlist=waitlist, enrolled=enrolled, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>')
def course_view(course_id):
    global admin
    #docs = get_course_section(course_id)
    if admin:
        sections = [{"_id": 12, 'professor': 'Amos Bloomberg', 'date': {'days': ['M', 'W'], 'startTime': '2:00PM', 'endTime': '3:15PM'}, 'capacity': 1, 'student': [ObjectId('635303beec3a435021103e89'), ObjectId(
            '635081d3c79712ba0de837cf')], 'waitlist': [ObjectId('6353040eec3a435021103e8a')], 'courseName': 'Software Engineering', 'courseID': 'CSCI-UA.474', '_id': ObjectId('635499bce6ec35919761b208'), 'name': 'Section 1'}]
        course = {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001", "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin",
                  "sections": sections}
        return render_template('admin_course.html', sections=sections, course=course, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)
    else:
        # query all courses that match the specified course code
        sections = [{"_id": 12, 'professor': 'Amos Bloomberg', 'date': {'days': ['M', 'W'], 'startTime': '2:00PM', 'endTime': '3:15PM'}, 'capacity': 1, 'student': [ObjectId('635303beec3a435021103e89'), ObjectId(
            '635081d3c79712ba0de837cf')], 'waitlist': [ObjectId('6353040eec3a435021103e8a')], 'courseName': 'Software Engineering', 'courseID': 'CSCI-UA.474', '_id': ObjectId('635499bce6ec35919761b208'), 'name': 'Section 1'}]
        course = {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001", "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin",
                  "sections": sections}
        return render_template('course.html', sections=sections, course=course, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>/add-section')
def create_section_view(course_id):
    global admin
    #docs = get_course_section(course_id)
    course = {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
              "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"}
    return render_template('create_section.html', course=course, admin=admin, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>/<section_id>/edit-section')
def edit_section_view(course_id, section_id):
    global admin
    section = {"_id": 12, 'professor': 'Amos Bloomberg', 'date': {'days': ['M', 'W'], 'startTime': '2:00PM', 'endTime': '3:15PM'}, 'capacity': 1, 'student': [ObjectId('635303beec3a435021103e89'), ObjectId(
        '635081d3c79712ba0de837cf')], 'waitlist': [ObjectId('6353040eec3a435021103e8a')], 'courseName': 'Software Engineering', 'courseID': 'CSCI-UA.474', '_id': ObjectId('635499bce6ec35919761b208'), 'name': 'Section 1'}
    #docs = get_course_section(course_id)
    course = {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
              "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"}
    return render_template('edit_section.html', course=course, admin=admin, section=section, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/courses/<course_id>/<section_id>/students')
def student_list_view(course_id, section_id):
    # course= get_course(course_id)
    # course_name= course['name']
    # course_code= course['courseID']
    # section_name = course['sections']['notes']
    # docs= get_students(course['sections']['student'])
    docs = [
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "Bar", "firstName": "Foo", "netID": "fb9876"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"},
        {"lastName": "LastName", "firstName": "FirstName", "netID": "abc123"}
    ]
    course = {"_id": 1, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
              "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"}
    section = {"_id": 12, 'professor': 'Amos Bloomberg', 'date': {'days': ['M', 'W'], 'startTime': '2:00PM', 'endTime': '3:15PM'}, 'capacity': 1, 'student': [ObjectId('635303beec3a435021103e89'), ObjectId(
        '635081d3c79712ba0de837cf')], 'waitlist': [ObjectId('6353040eec3a435021103e8a')], 'courseName': 'Software Engineering', 'courseID': 'CSCI-UA.474', '_id': ObjectId('635499bce6ec35919761b208'), 'name': 'Section 1'}
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
    # with open('../../database/courses.json', 'r') as f:
    #     docs = json.load(f)
    #     f.close()
    #docs= search_course(request.args.get('searchterm', ""))
    courses = [
        {"_id": 32, "courseID": "CSCI-UA.0001", "name": 'Intro to Computer Science', 'professor': 'Professor X',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
        {"_id": 32, "courseID": "CSCI-UA.0002", "name": 'Software Engineering', 'professor': 'Professor X',
            'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
            "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"},
        {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
            "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"},
        {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
            "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"},
        {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
            "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"},
        {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
            "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"},
        {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
            "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"},
        {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
            "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"},
        {"_id": 32, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001",
            "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin"},
    ]
    return render_template('course_search.html', courses=courses, admin=admin, username=username, successMsg=successMsg)


@app_blueprint.route('/cart')
def shopping_cart_view():
    #docs= get_cart(username)
    sections = [{"_id": 12, 'professor': 'Amos Bloomberg', 'date': {'days': ['M', 'W'], 'startTime': '2:00PM', 'endTime': '3:15PM'}, 'capacity': 1, 'student': [ObjectId('635303beec3a435021103e89'), ObjectId(
        '635081d3c79712ba0de837cf')], 'waitlist': [ObjectId('6353040eec3a435021103e8a')], 'courseName': 'Software Engineering', 'courseID': 'CSCI-UA.474', '_id': ObjectId('635499bce6ec35919761b208'), 'name': 'Section 1'}]
    return render_template('shopping_cart.html', sections=sections, admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/create-course')
def create_course_view():
    return render_template('create_course.html', admin=admin, username=username, errorMsg=errorMsg, successMsg=successMsg)


@app_blueprint.route('/edit-course/<course_id>')
def edit_course_view(course_id):
    # course=get_course(course_id)
    sections = [{"_id": 12, 'professor': 'Amos Bloomberg', 'date': {'days': ['M', 'W'], 'startTime': '2:00PM', 'endTime': '3:15PM'}, 'capacity': 1, 'student': [ObjectId('635303beec3a435021103e89'), ObjectId(
        '635081d3c79712ba0de837cf')], 'waitlist': [ObjectId('6353040eec3a435021103e8a')], 'courseName': 'Software Engineering', 'courseID': 'CSCI-UA.474', '_id': ObjectId('635499bce6ec35919761b208'), 'name': 'Section 1'}]
    course = {"_id": 1, "name": "Introduction to Computer Science", "courseID": "CSCI-UA.0001", "description":
              "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.", "admin": "admin",
              "sections": sections}
    return render_template('edit_course.html', admin=admin, course=course, errorMsg=errorMsg, successMsg=successMsg)
