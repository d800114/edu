from flask import Flask
app = Flask(__name__) 


from flask import render_template

@app.route ('/')
def contact():
    return render_template('file.html')

import os
from werkzeug.utils import secure_filename
from flask import request, redirect, url_for  


#deepseek Отсутствует функция allowed_file()
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#deepseek Отсутствует конфигурация UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = 'uploads'

#deepseek Даже если вы зададите UPLOAD_FOLDER, папка может не существовать.
#Нужно создать ее:
#os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

#deepseek Отсутствует маршрут для uploaded_file
from flask import send_from_directory
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/handle_file_upload', methods=['POST'])
def handle_file_upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
    return 'File upload unsuccessful'


if __name__ == '__main__':
    app.run(debug=True) 