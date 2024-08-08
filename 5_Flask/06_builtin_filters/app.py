from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def Main():
    obj = 'MLOps Engineering'
    conf = [1, 0.8, 0.3]
    return render_template('base.html',object = obj, output=False, confidences=conf)


if __name__ == '__main__':
    app.run(debug=True)