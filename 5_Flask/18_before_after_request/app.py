from flask import Flask, request, redirect, session, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = ';aksdjf;powiuefriu123'

########################
@app.before_request
def check_authentication():
    resticted_routes =['/dashboard', '/profile']
    if 'username' not in session and request.path in resticted_routes:
        print('Please log in to access this page!')
        return redirect(url_for('login'))

@app.after_request
def log_request_and_response(response):
    print(f'Request: {request.method} {request.path}_reponse status: {response.status}')
    return response


########################

@app.route('/')
def home():
    return 'Welcome to this page!'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('dashboard'))
    
    return '''<form method = 'post'> 
    <p> <input type= "text" name="username" placeholder="Enter username"></p>
    <p> <input type= "submit" value="login"></p>
    </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username')
    #flash('You have been logged out', 'info')
    return redirect(url_for('home'))


@app.route('/dashboard')
def dashboard():
    username = session['username']
    return f'Welcome, {username}, here is your dashboard, <a href="/logout">Logout</a>'


@app.route('/profile')
def profile():
    username = session['username']
    return f'Welcome, {username}, here is your profile, <a href="/logout">Logout</a>'



@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')




if __name__ == '__main__':
    app.run(debug=True)