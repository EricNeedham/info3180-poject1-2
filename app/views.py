s"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from app import db
from app.models import User
from .forms import UserForm
###
# Routing for your application.
###

@app.route('/profile/', methods=["GET", "POST"])
def profile():
  form = UserForm(csrf_enabled=False)
  if request.method == 'POST' and form.validate():
    user = User(form.first_name.data, form.last_name.data, form.age.data,
                    form.image.data)
    db_session.add(user)
    db.session.commit()
  return render_template('profile.html', form=form)

@app.route('/profiles/', method=["GET"])
def profiles():
  users = db.session.query(User).all()
  serializer = UserSchema(many=True)
  result = serializer.dump(users)
  return jsonify({'Users':result.data})

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/person')
def person():
  first_user = db.session.query(User).first()
  return "fisrt_name: {}, last_name: {}, age: {}, sex: {}, image: {}".format(first_user.fisrt_name, first_user.last_name, first_user.age, first_user.sex, first_user.image)
  

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
