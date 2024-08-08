from flask import Flask

app = Flask(__name__)

@app.route('/')
def Main():
    return "Hi This this the first session about flask."


@app.route('/blogs')
def Blogs():
    return 'these are newes your blogs!'


@app.route('/users')
def Users():
    users = ['ali', 'leyla', 'alborz']
    return f'the platform users list: {users}'

if __name__ == "__main__":
    app.run(debug=True)
