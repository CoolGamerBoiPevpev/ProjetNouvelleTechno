import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['inputName']
        password = request.form['inputPassword']
        email = request.form['inputEmail']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required.'
            
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password, email) VALUES (?, ?, ?)",
                    (username, generate_password_hash(password), email),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User or email already registered."
            else:
                #return redirect(url_for("auth.login"))
                #return redirect('/auth/index')
                return 'Je marche'
                exit

        return error

    return render_template('auth/signup.html')