# import the Flask class from the flask module
from flask import Flask, render_template
from flask import make_response
from flask import send_file


# create the application object
app = Flask(__name__)

# not sure what is going on here...
app.config['DEBUG'] = True


# note: we don't need to call run() since our application is embedded within the App Engine WSGI application server
# this means the following two lines of code are unnecessary... (how will i understand how to get around this shit?)
# if __name__ == '__main__':
# 	app.run(debug=True)


# this is the homepage of sorts
@app.route("/")
def home():
	return render_template("index.html")


# this is about page
@app.route("/about")
def about():
	return render_template("about.html")


# this is blog page
@app.route("/blog")
def blog():
	return render_template("blog.html")


# this is contact page
@app.route("/contact")
def contact():
	return render_template("contact.html")


# this is resume page
@app.route("/resume")
def resume():
	return render_template("resume.html")


# for handling errors
@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, nothing at this URL.', 404

