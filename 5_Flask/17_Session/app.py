from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = ';akdsjf;lj12458'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Hello, {username}, You are Logged in. <br> <a href="/logout">Logout</a> '
    return 'You are not logged in, please log in. <br> <a href="/login">Login</a> '




@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index'))
    
    return '''<form method = 'post'> 
    <p> <input type= "text" name="username" placeholder="Enter username"></p>
    <p> <input type= "submit" value="login"></p>
    </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))














if __name__ == '__main__':
    app.run(debug=True)
