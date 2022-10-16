from flask import Blueprint
from extensions import mongo

user_blueprint= Blueprint("users", __name__, url_prefix='/users')

@user_blueprint.route('/student/get/')
def get_student():
    student_collection = mongo.db.course
    students= student_collection.find()
    return students

@user_blueprint.route('/admin/get')
def get_admin():
    admin_collection = mongo.db.course
    admins= admin_collection.find()
    return admins
    
