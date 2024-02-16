# Created by Sazhod at 16.02.2024
import datetime

from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)

app.permanent_session_lifetime = datetime.timedelta(days=365)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.args.get('public_key'):
        session['public_key'] = request.args.get('public_key')
        return redirect('/profile', code=302)
    return render_template('index.html')


@app.route('/profile')
def profile():

    return render_template('profile.html')


def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
