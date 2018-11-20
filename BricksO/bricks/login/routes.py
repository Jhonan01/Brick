from flask import session, redirect, url_for, escape, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from bricks.login import login_bp

@login_bp.route('/login', methods = ['GET','POST'])
def login(): 

    return render_template('login.html')


@login_bp.route('/logout')
def logout():
    session.pop('usuario', 'usuario')
    return redirect(url_for('index'))

    
