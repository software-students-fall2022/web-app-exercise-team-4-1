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
