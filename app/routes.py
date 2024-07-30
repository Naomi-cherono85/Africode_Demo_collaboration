from flask import render_template, request, redirect, url_for
from app import db, app
from app.models import Testimonial

@app.route('/', methods = ["GET" ," POST "])
def index():
    return render_template('index.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('About.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        # Here you would typically save the data to a database or process it
         # Redirect after POST
    return render_template('Contact.html')

@app.route('/nutrition', methods=['GET', 'POST'])
def nutrition():
    return render_template('Nutrition.html')

@app.route('/fitness',methods=["GET","POST"])
def fitness():
    return render_template('fitness.html')

@app.route('/testimonials', methods=['GET', 'POST'])
def testimonials():
    return render_template('Testimonials.html', testimonials=testimonials)
