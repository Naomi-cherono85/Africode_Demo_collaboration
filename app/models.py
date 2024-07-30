from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __repr__(self):
        return f'<Testimonial {self.name}>'
