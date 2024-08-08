from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def Main():
    objs = ['car', 'bird', 'plane', 'ball']
    return render_template('base.html',objects = objs, output=False)


if __name__ == '__main__':
    app.run(debug=True)