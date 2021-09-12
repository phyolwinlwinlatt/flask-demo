from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('home.html')

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')

    name = request.form.get('name')
    password = request.form.get('password')
    if not name:
        return render_template('message.html', message = 'fill user name')
    if not password:
        return render_template('message.html', message= 'fill password')

    with sqlite3.connect("pythondemo.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from users where name = '%s'" % name)
    user = cur.fetchone()
    if not user:
        return render_template('message.html', message = 'no user found')

        # check user password
    elif  user[2] != password:
        return render_template('message.html', message= 'incorrect password')
    return render_template('profile.html', user = dict(user))
@app.route('/sign-up',  methods=['GET','POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')

    name = request.form.get('name')
    password = request.form.get('password')

    if not name:
        return render_template('message.html', message = 'fill name')
    if not password:
        return render_template('message.html', message='fill password')
    
    
    # create user
    with sqlite3.connect("pythondemo.db") as con:  
        cur = con.cursor()
        user = cur.execute("select name from users where name = '%s'" % name)
        if user:
            return render_template('message.html', message='user already exists')
        cur.execute("INSERT into Users (name, password) values (?,?)",(name, password))  
        con.commit()
    
    return render_template('message.html', message='successfully created')

@app.route('/users/<name>', methods=['GET', 'POST'])
def get_user(name):
    with sqlite3.connect("pythondemo.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()  
        cur.execute("select * from users where name = '%s'" % name )
        user = cur.fetchone()
    return render_template('profile.html', user = dict(user))


@app.route('/note', methods=['GET', 'POST'])
def note():
    if request.method == 'GET':
        return render_template('note.html')
    # create note
    with sqlite3.connect("pythondemo.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("insert into notes (body, user_id) values(?,?)",  (body, user_id))
    return ''
if __name__ == '__name__':
    app.run(debug= True)