from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE

@app.route("/")
def display_homepage():
    """Display homepage with link to application"""

    return render_template("index.html")


@app.route("/application-form")
def display_application():
    """Display a job application form"""

    roles = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html",
                           roles=roles)


@app.route("/application-success", methods=['POST'])
def process_application():
    """Process a job application form"""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    position = request.form.get('select')

    # Try to read in salary requirement as float
    try:
        salary = float(request.form.get('salary'))
    except ValueError:
        flash("Please enter a raw number with no commas for salary")
        return redirect('/application-form')

    return render_template("application-response.html",
                            fname=fname,
                            lname=lname,
                            salary=salary,
                            position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = True

    # Use the DebugToolbar
    #DebugToolbarExtension(app)


    app.run(host="0.0.0.0")
