<<<<<<< HEAD
from flask import Blueprint, render_template
import json

app_blueprint = Blueprint("app_blueprint", __name__)


@app_blueprint.route('/')
def home_view():
    # query all course codes in the students.json file under enrolled and cross-match with course data
    docs = [
        {"_id": 1, "status": "enrolled", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
        {"_id": 2, "waitlist_count": 12, "status": "on-waitlist", "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering',
            'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        {"_id": 3, "status": "enrolled", "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X',
            'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        {"_id": 4, "status": "enrolled", "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X',
            'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        {"_id": 5, "status": "enrolled", "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X',
            'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        {"_id": 6, "status": "enrolled", "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X',
            'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        {"_id": 7, "status": "enrolled", "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X',
            'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
    ]
    return render_template('student_courses.html', docs=docs)


@app_blueprint.route('/courses/<mongoid>')
def course_view(mongoid):
    # query all courses that match the specified course code
    docs = [
        {"_id": 1, "status": "open-section", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
        {"_id": 2, "waitlist_count": 12, "status": "closed", "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering',
            'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
    ]
    return render_template('course.html', docs=docs, course_name='Introduction to Computer Science', course_code="CSCI-UA.0001")


@app_blueprint.route('/courses')
def course_search_view():
    # query all courses in courses.json
    with open('../../database/courses.json', 'r') as f:
        docs = json.load(f)
        f.close()
    # docs = [
        # {"_id": 1, "status": "open", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
        #  {"_id": 2, "waitlist_count": 12, "status": "waitlist","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        #  {"_id": 3, "status": "closed","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        #  {"_id": 4, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        #  {"_id": 5, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        #  {"_id": 6, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        #  {"_id": 7, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
      #  ]
    return render_template('course_search.html', docs=docs)


@app_blueprint.route('/cart')
def shopping_cart_view():
    # query all course codes in the students.json file under cart and cross-match with course data
    docs = [
        {"_id": 1, "status": "cart", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X',
         'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
        {"_id": 2, "waitlist_count": 12, "status": "cart", "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering',
         'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
    ]
    return render_template('shopping_cart.html', docs=docs)
=======
from flask import Blueprint, render_template, request,redirect, url_for
from bson.json_util import dumps, loads, ObjectId
from .course import add_student, get_all_courses, get_course, get_course_section, search_course, remove_student
from .users.student import get_cart, get_student_courses, get_students
from .users.admin import get_admin_course
app_blueprint= Blueprint("app_blueprint", __name__)

admin = True
username = None

@app_blueprint.route('/')
def login_view():
    return render_template('login_page.html')

@app_blueprint.route('/sign-up')
def sign_up_view():
    return render_template('sign_up.html')

@app_blueprint.route('/home')
def home_view():
    if admin:
        docs = [
            {"max_students": 1, "_id": 1, "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        ]
        #docs= search_course(request.args.get('searchterm', ""))
        return render_template('admin_courses.html', docs=docs, admin=admin, username=username)
    else:
        docs = [
            {"max_students": 1, "_id": 1, "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        ]
        #docs= get_student_courses(username)
        return render_template('student_courses.html', docs=docs, admin=admin, username=username)
    
@app_blueprint.route('/courses/<course_id>')
def course_view(course_id):
    global admin
    #docs = get_course_section(course_id)
    if admin:
        docs = [
            {"max_students": 1, "_id": 1, "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
        ]
        return render_template('admin_course.html', docs=docs, course_name='Introduction to Computer Science', course_code="CSCI-UA.0001", admin=admin, username=username, course_id=2)
    else:
        docs = [
                {"students": [1,2], "max_students": 1, "_id": 1, "status": "open-section", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
                {"max_students": 1, "_id": 2, "waitlist_count": 12, "status": "closed","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
            ]
        return render_template('course.html', docs=docs, course_name='Introduction to Computer Science', course_code="CSCI-UA.0001", admin=admin, username=username, course_id=course_id)

@app_blueprint.route('/courses/<course_id>/add-section')
def create_section_view(course_id):
    global admin
    #docs = get_course_section(course_id)
    return render_template('create_section.html', course_name='Introduction to Computer Science', course_code="CSCI-UA.0001", admin=admin, course_id=course_id)

@app_blueprint.route('/courses/<course_id>/edit-section/<section_id>')
def edit_section_view(course_id, section_id):
    global admin
    section = {"professor": "Professor X", "capacity": 30, "notes": "This is a section", "date": {"days": ["Mo", "We"], "startTime": "9:30AM", "endTime": "10:45AM"}}
    #docs = get_course_section(course_id)
    return render_template('edit_section.html', course_name='Introduction to Computer Science', course_code="CSCI-UA.0001", admin=admin, course_id=course_id, section=section)

@app_blueprint.route('/courses/<course_id>/students')
def student_list_view(course_id):
    # course= get_course(course_id)
    # course_name= course['name']
    # course_code= course['courseID']
    # section_name = course['sections']['notes']
    # docs= get_students(course['sections']['student'])
    course_name = "Introduction to Computer Science"
    course_code = "CSCI-UA.0001"
    section_name = "X"
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
    return render_template('student_list.html', docs=docs, course_id=course_id, admin=admin, username=username, course_name=course_name, course_code=course_code, section_name=section_name)
    
@app_blueprint.route('/courses/<course_id>/students/add', methods=['GET','POST'])
def add_student_view(course_id):
    # course= get_course(course_id)
    # course_name=course['software engineering']
    # course_code=course['CS-474']
    # section_name=course['sections']['notes']

    if(request.method == 'POST'):
        studentId= request.form['studentId']
        add_student(studentId,course_id)
        return redirect(url_for('app_blueprint.student_list_view'))
    course_name = "Introduction to Computer Science"
    course_code = "CSCI-UA.0001"
    section_name = "X"
    return render_template('add_student.html', course_id=course_id, admin=admin, username=username, course_name=course_name, course_code=course_code, section_name=section_name)

@app_blueprint.route('/courses/<course_id>/students/remove', methods=['GET', 'POST'])
def remove_student_view(course_id):
    # course= get_course(course_id)
    # course_name=course['software engineering']
    # course_code=course['CS-474']
    # section_name=course['sections']['notes']
    if(request.method == 'POST'):
        studentId= request.form['studentId']
        remove_student(studentId,course_id)
        return redirect(url_for('app_blueprint.student_list_view'))

    course_name = "Introduction to Computer Science"
    course_code = "CSCI-UA.0001"
    section_name = "X"
    return render_template('remove_student.html', course_id=course_id, admin=admin, username=username, course_name=course_name, course_code=course_code, section_name=section_name)

@app_blueprint.route('/courses',methods=['GET'])
def course_search_view():
    #docs= search_course(request.args.get('searchterm', ""))
    docs = [
            {"max_students": 1, "_id": '63530541ec3a435021103e8d', "status": "open", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "status": "waitlist","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 3, "status": "closed","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 4, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 5, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 6, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 7, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
        ]
    return render_template('course_search.html', docs=docs, admin=admin, username=username)
    
@app_blueprint.route('/cart')
def shopping_cart_view():
    #docs= get_cart(username)
    docs = [
            {"max_students": 1, "_id": 1, "status": "cart", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "status": "cart","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        ]
    return render_template('shopping_cart.html', docs=docs, admin=admin, username=username)

@app_blueprint.route('/create-course')
def create_course_view():
    return render_template('create_course.html', admin=admin, username=username)

@app_blueprint.route('/edit-course/<course_id>')
def edit_course_view(course_id):
    course=get_course(course_id)
    course = {"_id": 1, "name": "Introduction to Computer Science", "code": "CSCI-UA.0001", "description": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."}
    return render_template('edit_course.html', admin=admin, course=course)
>>>>>>> cfd45e5138180ba14fd03a09cad6ad09c62674dd
