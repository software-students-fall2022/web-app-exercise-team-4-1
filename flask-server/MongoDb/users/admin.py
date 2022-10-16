from extensions import mongo
import course

def validate_admin_login(login):
    admin_collection = mongo.db.Admin
    admin= admin_collection.find({"username":login.username})
    if(admin.password== login.password):
        return admin
    else:
        return False

def add_admin_course(admin_username, course_id):
    admin_collection = mongo.db.Admin
    result= admin_collection.update_one({"username": admin_username}, {'$push': {'course_list': course_id}})
    course.add_course(course_id)
    return result.acknowledged

def remove_admin_course(admin_username, course_id):
    admin_collection = mongo.db.Admin
    result= admin_collection.update_one({"username": admin_username}, {'$pull': {'course_list': course_id}})
    course.remove_course(course_id)
    return result.acknowledged

def update_admin(username, new_value):
    admin_collection = mongo.db.Admin
    result= admin_collection.update_one({"username":username}, {"$set": new_value})
    return result.acknowledged