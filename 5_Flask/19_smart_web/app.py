from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from model import predict_price


app = Flask(__name__)

#app configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = ';aksdjf;kjkj;kj'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)


def login_required(f):
    def wrap(*args, **kwargs):
        if 'username' not in session:
            flash('You need to login first!', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pasword = bcrypt.generate_password_hash(password).decode('utf_8')

        new_user = User(username = username, password = hashed_pasword)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful, Please log in.', 'success')

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['username'] = user.username

            flash(' Login successful!', 'success')
            return redirect(url_for('input_data'))
        else:
            flash('Login failed, Check your username or password', 'danger')
        
    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('username')
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))


@app.route('/input' , methods=['GET', 'POST'])
@login_required
def input_data():
    if request.method == 'POST':
        featurs = [
            float(request.form['CRIM']), 
            float(request.form['ZN']), 
            float(request.form['INDUS']), 
            float(request.form['CHAS']), 
            float(request.form['NOX']), 
            float(request.form['RM']),
            float(request.form['AGE']), 
            float(request.form['DIS']), 
            float(request.form['RAD']), 
            float(request.form['TAX']), 
            float(request.form['PTRATIO']), 
            float(request.form['B']),
            float(request.form['LSTAT'] )
        ]

        predicted_price = predict_price(featurs)
        return render_template('result.html', price= predicted_price)
     
    return render_template('input.html')


@app.route('/result')
@login_required
def result():
    #dispaly outputed result.
    return render_template('result.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
