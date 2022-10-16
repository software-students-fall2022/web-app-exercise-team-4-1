from flask import Blueprint
from extensions import mongo

admin_blueprint= Blueprint("admin", __name__, url_prefix='/admin')

@admin_blueprint.route('/get')
def get_admin():
    admin_collection = mongo.db.Admin
    admins= admin_collection.find()
    return admins

@admin_blueprint.route('/add')
def add_admin():
    admin_collection = mongo.db.Admin
    admin_collection.insert_one()
    return "success"

@admin_blueprint.route('/remove')
def remove_admin():
    admin_collection = mongo.db.Admin
    admin_collection.delete_one()
    return "success"

@admin_blueprint.route('/update')
def update_admin():
    admin_collection = mongo.db.Admin
    admin_collection.update_one()
    return "success"