from flask import Flask
from flask import render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def Main():
    return render_template('home.html')


@app.route('/auth', methods=['POST', 'GET'])
def Authorization():

    if request.method=='GET':
        username = request.args.get('username')
        password = request.args.get('password')
    else:
        username = request.form['username']
        password = request.form['password']
    
    #username: ali, password:9876
    if username== 'ali' and password=='9876':
        #return redirect('https://www.google.com/')
        return redirect(url_for('Profile'))
    else:
        return redirect(url_for('Errors'))




@app.route('/profile')
def Profile():
    return 'Here is your profile!'


@app.route('/errors')
def Errors():
    return 'You are wrong!, check your password or username!'



if __name__ == '__main__':
    app.run(debug=True)