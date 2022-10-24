from flask import Blueprint, request, redirect, url_for
from models.mongodb import Database
from bson.json_util import dumps, loads, ObjectId
from ..course import get_all_courses, remove_student, add_student, get_courses
from routes import views
student_blueprint= Blueprint('student',__name__,url_prefix='/student')

@student_blueprint.route('/sign_up', methods=['GET','POST'])
def sign_up():
    Database.initialize()
    username=request.form['username']
    firstName=request.form['firstName']
    lastName=request.form['lastName']
    password=request.form['password']
    if (username and firstName and lastName and password):
        if(Database.count("Student",{"username":username})==0):
            Database.insert_one("Student", {'username': username,'firstName': firstName, 'lastName': lastName, 'password':password, 'course_list':[], 'carts':[], 'waitlist':[]})
            views.displayMsg="Reigstration Complete!"
            views.isError= False
            views.render='/'
            return redirect(url_for('app_blueprint.login_view'))
        else:
            views.displayMsg="Username is taken!"
            views.isError= True
            views.render='/sign-up'
            return redirect(url_for('app_blueprint.sign_up_view'))
    else:
        views.displayMsg="Please fill up all fields!"
        views.isError= True
        views.render='/sign-up'
        return redirect(url_for('app_blueprint.sign_up_view'))


def get_student_oid(username):
    return Database.find_single("Student", {"username": username})['_id']

def get_students(student_ids):
    courses = Database.find("Student", {"_id":{ "$in": [ObjectId(id) for id in student_ids] }})
    return loads(dumps(courses))

def get_student_courses():
    courses= Database.find_single("Student", {"username": views.username})['course_list']
    return get_courses(courses)

def get_student_sections():
    courses=get_student_courses()
    return get_sections(courses,ObjectId(get_student_oid(views.username)),'student')

def get_sections(courses, search, attribute):
    return([section for course in courses for section in course['sections'] if search in section[attribute]])

def get_student_waitlists():
    return get_sections(get_all_courses(),ObjectId(get_student_oid(views.username)),'waitlist')

@student_blueprint.route('/removecourse', methods=['GET','POST'])
def remove_course():
    section_id = request.form["section_id"]
    course_id= Database.find_single('Course', {'sections': {'$elemMatch':{'_id': ObjectId(section_id)}}})['_id']
    Database.update("Student", {"username": views.username}, {'$pull': {'course_list': ObjectId(course_id)}})
    remove_student(get_student_oid(views.username),course_id,section_id)
    views.displayMsg='Course has been removed'
    views.isError=False
    views.render='/home'
    return redirect(url_for('app_blueprint.home_view'))


@student_blueprint.route('/update_student',methods=['POST'])
def update_student():
    Database.initialize()
    new_values=request.form
    Database.update("Student",{"username":views.username}, {"$set": new_values})
    return "Update is complete!"

@student_blueprint.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    section_id = request.form["section_id"]
    if Database.count("Student",{"username": views.username, "carts":{"$in":[ObjectId(section_id)]}}) ==0:
        Database.update("Student", {"username": views.username}, {'$push': {'carts': ObjectId(section_id)}} )
        views.displayMsg="Courses section added to cart!"
        views.render="/course_search"
        views.isError=False
        return redirect(url_for('app_blueprint.course_search_view'))
    else:
        views.displayMsg="Course section already in cart!"
        views.render="/course_search"
        views.isError=True
        return redirect(url_for('app_blueprint.course_search_view'))

@student_blueprint.route('/get_cart')
def get_cart():
    carts= Database.find_single("Student",{"username":views.username},{'_id':0,'carts':1})['carts']
    courses= get_all_courses()
    return([section for course in courses for section in course['sections'] if section['_id'] in carts])

@student_blueprint.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    section_id=request.form['section_id']
    Database.update("Student", {"username": views.username}, {'$pull': {'carts': ObjectId(section_id)}} )
    views.displayMsg='Course section removed from cart!'
    views.render='/cart'
    views.isError=False
    return redirect(url_for('app_blueprint.shopping_cart_view'))

@student_blueprint.route('/remove_waitlist', methods=['POST'])
def remove_waitlist():
    section_id=request.form['section_id']
    Database.update("Course", { "sections._id": ObjectId(section_id)}, {'$pull': {'sections.$.waitlist': ObjectId(get_student_oid(views.username))}})
    views.displayMsg='Course section removed from waitlist!'
    views.render='/home'
    views.isError=False
    return redirect(url_for('app_blueprint.home_view'))
