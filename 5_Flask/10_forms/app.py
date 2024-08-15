from flask import Flask
from flask import render_template, request, redirect


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
        return 'we know you'
    else:
        return ' you are stranger!'


@app.route('/profile')
def Profile():
    return 'Here is your profile!'

if __name__ == '__main__':
    app.run(debug=True)