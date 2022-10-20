from email import message
from qbay import app
from flask import render_template, request, session, redirect
from qbay.login import login_checker, login_saving
from qbay.register import register, register_format_checker, register_saving
from qbay.updateUserProfile import update_user_checker, update_user_saving
from qbay.exceptions import InvalidRegister, InvalidLogin, InvalidUserUpdate
from qbay.db import db
import sqlite3


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            print(email)  # for testing
            try:
                # link the database to select user's email
                import os
                path = os.path.dirname(os.path.abspath(__file__))
                connection = sqlite3.connect(path + "/data.db")
                cursor = connection.cursor()
                row = cursor.execute("SELECT * FROM 'Users' "
                                     "WHERE email = email")
                # print(row)  # for testing
                # if found the email, store into user
                user = cursor.fetchone()
                connection.close()
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception:
                print(Exception)
                pass
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


# This function is used to connect the login.html
@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


# This function is used to get user information on the web
# check if the user can login based on the database
@app.route('/login', methods=['POST'])
def login_post():
    # get email and password
    email = request.form.get('email')
    password = request.form.get('password')

    # login checker input -> dic
    user = {
        "email": email,
        "password": password
    }

    # if info enter by user pass all the test below, user log in, else, fail
    try:
        login_checker(user)  # check the format

        # store the user email and password in row if find
        row = login_saving(user)
        if row != "None":
            # set the session logged_in to user's email
            session['logged_in'] = row[0]
        return redirect('/', code=303)
    except InvalidLogin as IL:
        return render_template('login.html',
                               message=IL.message)


# this function is used to show the home page once user log in
@app.route('/', endpoint='home')
@authenticate
def home(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals

    try:
        # link the database to fetch all properties
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM 'Properties';")
        all_prod = cursor.fetchall()
        # print(type(all_prod)) # for testing
        # print("it better fetched all") # for testing
        for prod in all_prod:
            print(prod)
        connection.close()
        return render_template('index.html', user=user, products=all_prod, message="")
    except Exception:
        # if there has been error loading properties, display err msg
        return render_template('index.html', user=user, products=[],
                               message="Soory! There has been an error loading the products")


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    acc_name = request.form.get('name')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    # if two passwords do not match, set error msg
    if password != password2:
        error_message = "The passwords do not match"
    else:
        user = {
            "acc_name": acc_name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        # find a way to displat the exception msg?
        try:
            register_format_checker(user)
            reg_user = register_saving(user)
            print(reg_user)
            register(reg_user)
            print("yes")
        except InvalidRegister as err:
            error_message = f"{err.message}"
        # try:
        #     # query to check if user already exists?
        #     register(reg_user)
        #     print("yes")
        # except:
        #     error_message = "Registration failed:("
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/update_user', methods=['GET'])
def update_user_get():
    """
    This function is used to find all the information of a user
    and shows on update_user.html
    """

    email = session['logged_in']  # get the email from session stored above
    print(email)  # for testing
    # connect the database
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    connection = sqlite3.connect(path + "/data.db")
    cursor = connection.cursor()

    # select all the info of the user
    row = cursor.execute("SELECT * FROM 'Users' WHERE email = email")
    print(row)  # for testing
    user = cursor.fetchone()
    connection.close()
    print(user)

    # store another session which is id
    session['id'] = user[0]

    # if fetch success, return user info on the web
    if user:
        return render_template('update_user.html',
                               user=user, message='connect')
    else:
        return render_template('update_user.html',
                               message='failed')


# This function is to connect user
# to update_user_save.html if they click on update
@app.route('/update_user_save', methods=['GET'])
def update_user_get2():
    # templates are stored in the templates folder
    return render_template('update_user_save.html',
                           message='Please Enter Info')


"""
This function is used to update all the information user entered 
and re-shows everything update to them
"""


@app.route('/update_user_save', methods=['POST'])
def update_user_save():
    # templates are stored in the templates folder
    # get all the info enter from web
    Email = request.form.get('email')
    Password = request.form.get('password')
    Name = request.form.get('name')
    Billing_Address = request.form.get('billing_address')
    Postal_Code = request.form.get('Postal_Code')

    # store in a dic so it can be used as input
    user = {
        "acc_name": Name,
        "email": Email,
        "password": Password,
        "address": Billing_Address,
        "postal_code": Postal_Code
    }
    id = session['id']

    # if update success, return back to update_user.html, else, fail
    try:
        update_user_checker(user)  # check the format
        update_user_saving(user, id)  # check the database

        # connect the database
        import os
        path = os.path.dirname(os.path.abspath(__file__))
        connection = sqlite3.connect(path + "/data.db")
        cursor = connection.cursor()

        # select all the info based on user id
        row = cursor.execute("SELECT * FROM 'Users' "
                             "WHERE user_id = (?)", (id,))
        print(row)  # for testing
        user = cursor.fetchone()  # store info fetch into user
        connection.close()
        if user:
            return render_template('update_user.html', user=user,
                                   message='Hi!Below is your Information')
    except InvalidUserUpdate as IUU:
        return render_template('update_user_save.html',
                               message=IUU.message)


# log out of the web
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')
