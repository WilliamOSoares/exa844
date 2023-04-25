from flask import Flask,session, render_template, request, make_response, redirect
from datetime import datetime, timedelta, timezone

app = Flask(__name__, template_folder="templates")
#app.config()

@app.route("/")
def counter():
    counter_value = request.args.get('counter',default=0, type=int) + 1
    
    if 'counterCookie' in request.cookies:
        count = int(request.cookies.get('counterCookie'))
    else:
        count = 1
        counter_value=1        
    resp = make_response(render_template('index.html', counterCookie=count, counter=counter_value))
    resp.set_cookie('counterCookie', str(count + 1).encode('utf-8'), max_age=60*60)
    return resp

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    session['_creation_time'] = datetime.now(timezone.utc)
    return redirect('/')

@app.route('/', methods=['GET'])
def home():
    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc) - session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time
        return f'Hello, {username}! Your session will expire in '+ str(remaining_time)+' seconds. <a href="/logout">Logout</a>'
    else:
        return 'Welcome to Flask Session Example! <a href="/login">Login</a>'

if __name__ == '__main__':
    app.run(debug=True)