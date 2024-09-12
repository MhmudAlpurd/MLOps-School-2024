from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    return 'Here is a simple page for handling errors in Flask!'


@app.route('/error')
def Error():
    abort(500)
    return 'error'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def internal_server_erorr(e):
    return render_template('500.html')



if __name__ == '__main__':
    app.run(debug=True)