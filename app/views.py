from flask import Blueprint, render_template, request, redirect, session, url_for
from .models import User, Job, Application
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return redirect(url_for('views.login'))

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user'] = user.username
            return redirect(url_for('views.jobs'))
    return render_template('login.html')

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('views.login'))
    return render_template('signup.html')

@views.route('/jobs')
def jobs():
    if 'user' not in session:
        return redirect(url_for('views.login'))
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@views.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resume = request.form['resume']
        application = Application(name=name, email=email, resume=resume, job_id=job_id)
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('views.jobs'))
    job = Job.query.get(job_id)
    return render_template('apply.html', job=job)
