from extensions import mongo

def get_section(course_id):
    section_collection = mongo.db.Section
    section= section_collection.find({"id": course_id})
    return section

def add_section(section):
    section_collection = mongo.db.Section
    if(section_collection.find({"id":section.id}).count()==0):
        result=section_collection.insert_one(section)
        return result.acknowledged
    else:
        return False

def remove_section(course_id):
    section_collection = mongo.db.Section
    result=section_collection.delete_one({"id":course_id})
    return result.acknowledged

def update_section(course_id, new_value):
    section_collection = mongo.db.Section
    result= section_collection.update_one({"id":course_id}, {"$set": new_value})
    return result.acknowledged