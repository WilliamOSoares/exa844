from flask import Flask,session, render_template, request, make_response, redirect
from datetime import datetime, timedelta, timezone

app = Flask(__name__, template_folder="templates")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'

@app.route("/")
def main():
    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc) -
                        session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time
        counter_value = request.args.get('counter', default=0, type=int) + 1
        count = request.cookies.get('counterCookie')

        resp = render_template('index.html', counter=counter_value, username=username, remaining_time=remaining_time, counterCookie=count)
    else:
        if 'counterCookie' in request.cookies:
            count = request.cookies.get('counterCookie')
        else:
            count = "0"
        resp = render_template('login.html')   
    return resp

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    session['_creation_time'] = datetime.now(timezone.utc)

    if 'counterCookie' in request.cookies:
        count = int(request.cookies.get('counterCookie'))
    else:
        count = 1
    resp = redirect('/')     
    resp.set_cookie('counterCookie', str(count + 1).encode('utf-8'), max_age=60*60*24)

    return resp

if __name__ == '__main__':
    app.run(debug=True)