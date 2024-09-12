from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '1246887sdf215sd'

@app.route('/')
def index():
    flash('Welcome to this course!')
    return render_template('index.html')


@app.route('/success')
def success():
    flash('You have successfully completed your action!', 'success')
    return redirect(url_for('index'))


@app.route('/error')
def error():
    flash('You are worng', 'error')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)