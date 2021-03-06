from mongoengine import *
from models import *
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)
connect('tumblelog')


# CREATE
@app.route('/createuser', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        # TODO: Implement validation
        newuser = User(email=request.form['email'])
        newuser.first_name = request.form['first_name']
        newuser.last_name = request.form['last_name']
        newuser.save()
        return jsonify(request.form)
    else:
        return "nothing"


# READ
@app.route('/listusers', methods=['GET'])
def listusers():
    if request.method == 'GET':
        users = [user.first_name for user in User.objects]

        return jsonify(users)
    else:
        return "nothing"

# TODO: UPDATE
# TODO: DELETE
# TODO: Convert to PEP8 
# TODO: Convert to Flask_RESTPlus
# TODO: Research & incorporate methods for avoiding any possible MongoDB version of SQL injection
# TODO: Create Tests for functions
# TODO: Break functions out of routes into their own folder structure for each route
# TODO: Move any shared business logic /service layers to a utilities folder or a core folder


if __name__ == '__main__':
    app.run()