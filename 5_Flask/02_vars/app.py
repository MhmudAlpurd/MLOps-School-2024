from flask import Flask

app = Flask(__name__)

@app.route('/')
def Main():
    return 'Hi friend!'


@app.route('/userprofile/<string:username>')
def UserProfile(username):
    return f'this page belongs to {username}'







if __name__ == '__main__':
    app.run(debug=True)