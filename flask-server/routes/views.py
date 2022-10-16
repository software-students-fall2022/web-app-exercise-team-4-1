from flask import Blueprint, render_template
import routes.course

app_blueprint= Blueprint("app_blueprint", __name__)

@app_blueprint.route('/')
def home_view():
    return render_template('base.html')

@app_blueprint.route('/course/<mongoid>')
def course_view(mongoid):
    doc = routes.course.get_course
    #doc = {"name": 'Course Name', 'professor': 'Professor Name', 'course_description': 'Doggo ipsum puggo wrinkler shoober big ol pupper, wow such tempt. Bork smol borking doggo with a long snoot for pats doggo wow very biscit much ruin diet, what a nice floof wrinkler. Ur givin me a spook very hand that feed shibe floofs pupper, bork. Floofs adorable doggo big ol you are doing me the shock, doggorino tungg. Vvv heck thicc many pats clouds puggorino boofers pupper, heckin good boys and girls heckin many pats doggorino many pats. You are doin me a concern doing me a frighten wow very biscit long woofer boof wow such tempt, smol wrinkler borking doggo extremely cuuuuuute. borkdrive shooberino pats. Big ol pupper fat boi snoot heck wow very biscit most angery pupper I have ever seen I am bekom fat, tungg very hand that feed shibe many pats shibe blep. Most angery pupper I have ever seen sub woofer h*ck, stop it fren.Doggo ipsum puggo wrinkler shoober big ol pupper, wow such tempt. Bork smol borking doggo with a long snoot for pats doggo wow very biscit much ruin diet, what a nice floof wrinkler. Ur givin me a spook very hand that feed shibe floofs pupper, bork. Floofs adorable doggo big ol you are doing me the shock, doggorino tungg. Vvv heck thicc many pats clouds puggorino boofers pupper, heckin good boys and girls heckin many pats doggorino many pats. You are doin me a concern doing me a frighten wow very biscit long woofer boof wow such tempt, smol wrinkler borking doggo extremely cuuuuuute. borkdrive shooberino pats. Big ol pupper fat boi snoot heck wow very biscit most angery pupper I have ever seen I am bekom fat, tungg very hand that feed shibe many pats shibe blep. Most angery pupper I have ever seen sub woofer h*ck, stop it fren.'}
    return render_template('course.html', mongoid=mongoid, doc=doc)
    

    