from flask import Flask
from routes import views, course, users
from extensions import mongo

app= Flask(__name__)
app.register_blueprint(views.app_blueprint)
app.register_blueprint(course.course_blueprint)
app.register_blueprint(users.user_blueprint)

if __name__=='__main__':
    app.run(debug=True)
    mongo.init_app(app)

