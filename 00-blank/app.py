from flask import Flask
app = Flask(__name__) 

from flask import render_template
@app.route ('/')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True) 