from extensions import mongo
from section import remove_section

def get_all_courses():
    course_collection = mongo.db.Course
    courses= course_collection.find()
    return courses

def get_course(course_id):
    course_collection = mongo.db.Course
    courses= course_collection.find({"id":course_id})
    return courses


def add_course(course):
    courses_collection = mongo.db.Course
    if(courses_collection.find({"id":course.id}).count()==0):
        result=courses_collection.insert_one(course)
        return result.acknowledged
    else:
        return False

def remove_course(course_id):
    courses_collection = mongo.db.Course
    result=courses_collection.delete_one({"id":course_id})
    if(result.acknowledged):
        remove_section(course_id)
    return result.acknowledged

def update_course(course_id, new_value):
    courses_collection = mongo.db.Course
    result= courses_collection.update_one({"id":course_id}, {"$set": new_value})
    return result.acknowledged