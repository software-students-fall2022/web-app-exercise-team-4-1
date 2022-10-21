from flask import Blueprint, request, redirect, url_for
from models.mongodb import Database
from bson.json_util import dumps, loads,ObjectId
from routes.views import *
authenticate_blueprint= Blueprint('authenticate',__name__)

@authenticate_blueprint.route('/login', methods=['POST'])
def validate_login():
    username= request.form["username"]
    password= request.form["password"]
    Database.initialize()
    student_status= validate_student_login(username,password)
    admin_status= validate_student_login(username,password)

    if (student_status or admin_status):
        if(student_status):
            admin=False
        else:
            admin=True
        return redirect(url_for('app_blueprint.home_view'))
    else:
        Database.close()
        return redirect(url_for('app_blueprint.login_view'))


def validate_student_login(username, password):
    username= request.form["username"]
    password= request.form["password"]
    student_count = Database.count("Student", {"username" : username})
    if(student_count ==0):
        return False
    else:
        student = Database.find_single("Student", {"username" : username})
        if(student['password'] == password):
            return dumps(student)

def validate_admin_login(username, password):
    username= request.form["username"]
    password= request.form["password"]
    admin_count = Database.count("Admin", {"username" : username})
    if(admin_count==0):
        return False
    else:
        admin = Database.find_single("Admin", {"username" : username})
        if(admin.password == password):
            return dumps(admin)
