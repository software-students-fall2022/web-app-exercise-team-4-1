from flask import Blueprint, render_template, request
from .course import get_all_courses, search_course
from .users.student import get_cart
app_blueprint= Blueprint("app_blueprint", __name__)

admin = True
student_username = "testUser"

@app_blueprint.route('/')
def home_view():
    global admin
    global student_username
    if admin:
        docs = [
            {"max_students": 1, "_id": 1, "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        ]
        return render_template('admin_courses.html', docs=docs, admin=admin, student_username=student_username)
    else:
        docs = [
            {"max_students": 1, "_id": 1, "status": "enrolled", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "status": "on-waitlist","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 3, "status": "enrolled","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 4, "status": "enrolled","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 5, "status": "enrolled","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 6, "status": "enrolled","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 7, "status": "enrolled","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
        ]
        return render_template('student_courses.html', docs=docs, admin=admin, student_username=student_username)
    
@app_blueprint.route('/courses/')
def course_view():
    global admin
    global student_username
    if admin:
        docs = [
            {"max_students": 1, "_id": 1, "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
        ]
        return render_template('admin_course.html', docs=docs, course_name='Introduction to Computer Science', course_code="CSCI-UA.0001", admin=admin, student_username=student_username)
    else:
        docs = [
                {"students": [1,2], "max_students": 1, "_id": 1, "status": "open-section", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
                {"max_students": 1, "_id": 2, "waitlist_count": 12, "status": "closed","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
            ]
        return render_template('course.html', docs=docs, course_name='Introduction to Computer Science', course_code="CSCI-UA.0001", admin=admin, student_username=student_username)
    
@app_blueprint.route('/courses/<search>')
def course_search_view(search):
    #docs = search_course(search)
    global admin
    global student_username
    docs = [
            {"max_students": 1, "_id": 1, "status": "open", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "status": "waitlist","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 3, "status": "closed","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 4, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 5, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 6, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"max_students": 1, "_id": 7, "status": "open","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
        ]
    return render_template('course_search.html', docs=docs, admin=admin, student_username=student_username)
    
@app_blueprint.route('/cart')
def shopping_cart_view():
    #docs= get_cart()
    global admin
    global student_username
    docs = [
            {"max_students": 1, "_id": 1, "status": "cart", "code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"max_students": 1, "_id": 2, "waitlist_count": 12, "status": "cart","code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
        ]
    return render_template('shopping_cart.html', docs=docs, admin=admin, student_username=student_username)

@app_blueprint.route('/create-course')
def create_course_view():
    global admin
    return render_template('create_course.html', admin=admin)