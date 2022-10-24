from cgitb import reset
from distutils.log import error
from flask import Blueprint, render_template, request, redirect, url_for
from .users.admin import get_admin_course
from .users.student import get_cart, get_student_courses, get_student_oid, get_students, get_student_sections, get_student_waitlists
from .course import add_student, get_all_courses, get_course, get_course_section, search_course, remove_student
from bson.json_util import dumps, loads, ObjectId
from flask import Blueprint, render_template
import json

app_blueprint = Blueprint("app_blueprint", __name__)

admin = None
username = None
isError = False
displayMsg = None
render = None


def reset_message(render_page):
    if (render != render_page):
        global displayMsg
        displayMsg = None


@app_blueprint.route('/')
def login_view():
    reset_message('/')
    return render_template('login_page.html', displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/sign-up')
def sign_up_view():
    reset_message('/sign-up')
    return render_template('sign_up.html', displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/sign-up/admin')
def admin_sign_up_view():
    reset_message('/sign-up/admin')
    return render_template('admin_sign_up.html', displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/home')
def home_view():
    reset_message('/home')
    if admin:
        courses = search_course(request.args.get('searchterm', ""))
        return render_template('admin_courses.html', courses=courses, admin=admin, username=username, displayMsg=displayMsg, isError=isError)
    else:
        enrolled = get_student_sections()
        waitlist = get_student_waitlists()
        for section in waitlist:
            for index,id in enumerate(section['waitlist']):
                if(id==get_student_oid(username)):
                    section['waitlistPosition']=index+1
        
        return render_template('student_courses.html', waitlist=waitlist, enrolled=enrolled, admin=admin, username=username, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/courses/<course_id>')
def course_view(course_id):
    reset_message('/courses')
    course = get_course(course_id)
    sections = course['sections']
    if admin:
        return render_template('admin_course.html', sections=sections, course=course, admin=admin, username=username, displayMsg=displayMsg, isError=isError)
    else:
        return render_template('course.html', sections=sections, course=course, admin=admin, username=username, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/courses/<course_id>/add-section')
def create_section_view(course_id):
    reset_message('/add-section')
    course = get_course(course_id)
    return render_template('create_section.html', course=course, admin=admin, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/courses/<course_id>/<section_id>/edit-section')
def edit_section_view(course_id, section_id):
    reset_message('/edit-section')
    course = get_course(course_id)
    section = [sections for sections in course['sections']
               if sections['_id'] == ObjectId(section_id)][0]
    return render_template('edit_section.html', course=course, admin=admin, section=section, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/courses/<course_id>/<section_id>/students')
def student_list_view(course_id, section_id):
    reset_message('courses/students')
    course = get_course(course_id)
    section = [section for section in course['sections']
               if section['_id'] == ObjectId(section_id)][0]
    docs = get_students(section['student'])
    return render_template('student_list.html', docs=docs, course=course, admin=admin, username=username, section=section, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/courses/<course_id>/<section_id>/students/add', methods=['GET', 'POST'])
def add_student_view(course_id, section_id):
    reset_message('/add_student')
    course = get_course(course_id)
    section = [section for section in course['sections']
               if section['_id'] == ObjectId(section_id)][0]
    return render_template('add_student.html', course=course, admin=admin, username=username, section=section, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/courses/<course_id>/<section_id>/students/remove', methods=['GET', 'POST'])
def remove_student_view(course_id, section_id):
    reset_message('/remove_student')
    course = get_course(course_id)
    section = [section for section in course['sections']
               if section['_id'] == ObjectId(section_id)][0]
    return render_template('remove_student.html', course=course, admin=admin, username=username, section=section, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/courses', methods=['GET'])
def course_search_view():
    reset_message('/course_search')
    courses = search_course(request.args.get('searchterm', ""))
    return render_template('course_search.html', courses=courses, admin=admin, username=username, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/cart')
def shopping_cart_view():
    reset_message('/cart')
    sections = get_cart()
    return render_template('shopping_cart.html', sections=sections, admin=admin, username=username, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/create-course')
def create_course_view():
    reset_message('/create-course')
    return render_template('create_course.html', admin=admin, username=username, displayMsg=displayMsg, isError=isError)


@app_blueprint.route('/edit-course/<course_id>')
def edit_course_view(course_id):
    reset_message('/edit-course')
    course = get_course(course_id)
    return render_template('edit_course.html', admin=admin, course=course, displayMsg=displayMsg, isError=isError)
