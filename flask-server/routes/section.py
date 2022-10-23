from flask import Blueprint, request
from models.mongodb import Database

section_blueprint= Blueprint('section',__name__,url_prefix='/section')

@section_blueprint.route('/get/<course_id>')
def get_section(course_id):
    section= Database.find("Section", {"id": course_id})
    return section

@section_blueprint.route('/add',methods=['POST'])
def add_section():
    request_data=request.json
    result=Database.insert("Section", request_data)
    return result.acknowledged

@section_blueprint.route('/remove', methods=['POST'])
def remove_section():
    request_data= request.json
    result=Database.delete("Section",{"id":request_data.id})
    return result.acknowledged
