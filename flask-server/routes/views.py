from flask import Blueprint, render_template

app_blueprint= Blueprint("app_blueprint", __name__)

@app_blueprint.route('/')
def home_view():
    return render_template('index.html')

@app_blueprint.route('/courses/<mongoid>')
def course_view(mongoid):
    doc = {"code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
    return render_template('course.html', mongoid=mongoid, doc=doc)
    
@app_blueprint.route('/courses')
def course_search_view():
    docs = [
            {"code": "CSCI-UA.0001", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Intro to Computer Science', 'professor': 'X', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in finibus dolor. Ut ut sollicitudin ante. Praesent fringilla augue ante, vitae feugiat nisl consequat ut.'},
            {"code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'},
            {"code": "CSCI-UA.0002", "section": "X", "date": {"days": ["T", "Th"], "start_time": "9:30AM", "end_time": "10:45AM"}, "name": 'Software Engineering', 'professor': 'X', 'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia.'}
        ]
    return render_template('course_search.html', docs=docs)
    
    