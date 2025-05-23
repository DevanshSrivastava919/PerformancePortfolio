import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key_for_development")

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Render the projects page."""
    return render_template('projects.html')

@app.route('/resume')
def resume():
    """Render the resume page."""
    return render_template('resume.html')

@app.route('/download_resume')
def download_resume():
    """Download resume PDF."""
    return send_from_directory('static', 'resume.pdf')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Render the contact page and handle form submissions."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Log the form data (in a real app, you would send an email or save to a database)
        app.logger.info(f"Contact form submission - Name: {name}, Email: {email}, Message: {message}")
        
        # Flash a success message
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
