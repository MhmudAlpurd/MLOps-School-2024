from flask import Flask, render_template, url_for, request, flash, redirect
import os

app = Flask(__name__)
app.secret_key = 'a;sdklfj;lkajdsf;lkj'

app.config['UPLOAD_FOLDER']='uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('assign a file, please')
        return redirect(request.url)

    file = request.files['file']
    if file.filename=='':
        flash('No Selected file')
        return redirect(request.url)
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        flash('File successfully uploaded')
        return redirect(url_for('index'))

        #image_1.jpg
        #/uploads
        #/uploads/image_1.jpg

    
    











if __name__ == '__main__':
    app.run(debug=True)