from flask import Flask, render_template, url_for

app= Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/course/<mongoid>')
def course_view(mongoid):
    """
    Routes for GET requests to the course page
    Displays the details of a course
    """

    doc = {"name": 'Course Name', 'professor': 'Professor Name', 'course_description': 'Doggo ipsum puggo wrinkler shoober big ol pupper, wow such tempt. Bork smol borking doggo with a long snoot for pats doggo wow very biscit much ruin diet, what a nice floof wrinkler. Ur givin me a spook very hand that feed shibe floofs pupper, bork. Floofs adorable doggo big ol you are doing me the shock, doggorino tungg. Vvv heck thicc many pats clouds puggorino boofers pupper, heckin good boys and girls heckin many pats doggorino many pats. You are doin me a concern doing me a frighten wow very biscit long woofer boof wow such tempt, smol wrinkler borking doggo extremely cuuuuuute. borkdrive shooberino pats. Big ol pupper fat boi snoot heck wow very biscit most angery pupper I have ever seen I am bekom fat, tungg very hand that feed shibe many pats shibe blep. Most angery pupper I have ever seen sub woofer h*ck, stop it fren.Doggo ipsum puggo wrinkler shoober big ol pupper, wow such tempt. Bork smol borking doggo with a long snoot for pats doggo wow very biscit much ruin diet, what a nice floof wrinkler. Ur givin me a spook very hand that feed shibe floofs pupper, bork. Floofs adorable doggo big ol you are doing me the shock, doggorino tungg. Vvv heck thicc many pats clouds puggorino boofers pupper, heckin good boys and girls heckin many pats doggorino many pats. You are doin me a concern doing me a frighten wow very biscit long woofer boof wow such tempt, smol wrinkler borking doggo extremely cuuuuuute. borkdrive shooberino pats. Big ol pupper fat boi snoot heck wow very biscit most angery pupper I have ever seen I am bekom fat, tungg very hand that feed shibe many pats shibe blep. Most angery pupper I have ever seen sub woofer h*ck, stop it fren.'}
    return render_template('course.html', mongoid=mongoid, doc=doc)
    
if __name__=='__main__':
    app.run(debug=True)