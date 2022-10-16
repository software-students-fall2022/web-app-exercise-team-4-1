from extensions import mongo

def validate_student_login(login):
    student_collection = mongo.db.Student
    student= student_collection.find({"username":login.username})
    if(student.password== login.password):
        return student
    else:
        return False

def add_course(student_username, course_id):
    student_collection = mongo.db.Student
    result= student_collection.update_one({"username": student_username}, {'$push': {'course_list': course_id}})
    return result.acknowledged

def remove_course(student_username, course_id):
    student_collection = mongo.db.Student
    result= student_collection.update_one({"username": student_username}, {'$pull': {'course_list': course_id}})
    return result.acknowledged

def update_student(username, new_value):
    student_collection = mongo.db.Student
    result= student_collection.update_one({"username":username}, {"$set": new_value})
    return result.acknowledged