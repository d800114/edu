from flask import Flask
app = Flask(__name__) #экземпляр класса Flask

@app.route('/')       #дек.какой url должен вызывать функцию
def hello_world():
    return """Hello, World!<br><br>
              <a href="http://127.0.0.1:5000/Ivan">Ivan
              <i>(или ввести другое имя)</i></a><br>
              <a href="http://127.0.0.1:5000/post/123">Post NNN
              <i>(или ввести другой номер)</i></a>
            """ 
    
from flask import render_template

@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # показать пост с заданным id, id - целое число
    return f'Post {post_id}'

if __name__ == '__main__':
    app.run(debug=True)    #запуск приложения на локальном сервере разработки
                           #debug - позволятет отображать ошибки на локальной
                           #веб-странице

