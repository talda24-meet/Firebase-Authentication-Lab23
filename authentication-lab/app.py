from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

const firebaseConfig = {
    "apiKey": "AIzaSyDEyKgkZwD9gOORsunsw8Sl0wB4Dr7v7Ro",
    "authDomain": "taltest-a00ba.firebaseapp.com",
    "projectId": "taltest-a00ba",
    "storageBucket": "taltest-a00ba.appspot.com",
    "messagingSenderId": "453121566224",
    "appId": "1:453121566224:web:b5bf83f6900995b7048c95",
    "measurementId": "G-4QSQ8F5582"
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
    try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('add_tweet.html'))
    except:
        error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)