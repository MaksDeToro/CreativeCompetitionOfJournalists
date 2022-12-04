from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('file_1.html')


@app.route('/login', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    return render_template('Login.html', message=message)


@app.route('/register')
def register():
    return render_template('Register.html')


app.route('/personal_area')
def personal_area():
    return render_template('Personal Area.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')