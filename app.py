


import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key_for_development")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/download_resume')
def download_resume():
    return send_from_directory(app.static_folder, 'resume.pdf')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        app.logger.info(f"Contact form submission - Name: {name}, Email: {email}, Message: {message}")
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
