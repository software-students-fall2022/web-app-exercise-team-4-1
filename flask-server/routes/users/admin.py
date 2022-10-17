from flask import Blueprint, request
from models.mongodb import Database

admin_blueprint= Blueprint('admin',__name__,url_prefix='/admin')


@admin_blueprint.route('/login/', methods=['POST'])
def validate_admin_login():
    username= request.form["username"]
    password= request.form["password"]
    
    Database.initialize()
    admin = Database.find("Admin", {"username":username})
    if(admin is not None and admin.password== password):
        return admin
    else:
        Database.close()
        return False

@admin_blueprint.route('/addcourse/<username>/<course_id>')
def add_admin_course(admin_username, course_id):

    result= Database.update("Admin", {"username": admin_username}, {'$push': {'course_list': course_id}})
    return result.acknowledged

@admin_blueprint.route('/removecourse/<admin_username>/<course_id>')
def remove_admin_course(admin_username, course_id):
    result= Database.update("Admin", {"username": admin_username}, {'$pull': {'course_list': course_id}})
 #   course.remove_course(course_id)
    return result.acknowledged

@admin_blueprint.route('/update',methods=["POST"])
def update_admin(username):
    new_values= request.json
    result= Database.update("Admin", {"username":username}, {"$set": new_values})
    return result.acknowledged