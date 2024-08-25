from flask import Flask
from flask import render_template, request, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'asdfakjsd;fiowerpoui'

@app.route('/')
def Main():
    return 'welcome to this application'


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()

    if request.method == 'POST':
        #if form.validate_on_submit():
        if form.validate():
            username = request.form['username']
            password = request.form['password']
            if username == 'ali'  and password =='123':
                return redirect(url_for('Panel'))
            else:
                return redirect(url_for('Error_Login'))
        else:
            return 'check!'
    return render_template('login.html', form=form)


@app.route('/panel')
def Panel():
    return 'Here is your PANEL!'


@app.route('/errors')
def Error_Login():
    return 'Your are not our customer!'


if __name__ == '__main__':
    app.run(debug=True)