from flask import Flask
from routes import views, course, authenticate
from routes.users import admin, student

app=Flask(__name__)

app.register_blueprint(views.app_blueprint)
app.register_blueprint(course.course_blueprint)
app.register_blueprint(student.student_blueprint)
app.register_blueprint(admin.admin_blueprint)
app.register_blueprint(authenticate.authenticate_blueprint)

if __name__=='__main__':
    app.run(debug=True)

