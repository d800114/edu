from flask import Flask
app = Flask(__name__) 

from flask import render_template
@app.route ('/')
def contact():
    return render_template('contact.html')

from flask import request, redirect, url_for
@app.route('/handle_form', methods= ['POST'])
def handle_form():
    name = request.form['name']
    email = request.form['email']
    # Обработать или сохранить данные формы
    print(f"Получено: Имя={name}, Email={email}")  # Для отладки
    return redirect(url_for('thank_you'))


@app.route('/thank_you')
def thank_you():
    return "<h1>Спасибо!</h1><p>Форма успешно отправлена.</p>"


if __name__ == '__main__':
    app.run(debug=True) 