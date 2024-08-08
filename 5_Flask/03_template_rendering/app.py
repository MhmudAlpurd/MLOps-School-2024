from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def Main():
    objs = ['car', 'bird', 'plane', 'ball']
    return render_template('base.html',objects = objs, model_name='yolov10')


@app.route('/courses')
def Courses():
    return render_template('courses.html')

@app.route('/login')
def Login():
    return 'login'


if __name__ == '__main__':
    app.run(debug=True)