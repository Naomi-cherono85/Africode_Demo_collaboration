# Project Title: Fitness and Nutrition Website

## Project Description
This is a Flask-based website that provides information about fitness, nutrition, and testimonials. The website includes various pages such as home, about, contact, nutrition, fitness, and testimonials. Users can submit testimonials through the website.

## Features
- Responsive design using Bootstrap
- User-friendly interface
- Contact form with validation
- Testimonials section with pagination
- Database integration using SQLAlchemy

## Collaboration Process
This project was developed using the following collaboration process:

1. **Planning and Design**: The project was initially planned and designed by a team of developers. They discussed the requirements, wireframes, and user stories.

2. **Code Review**: The code was reviewed by other team members to ensure it adhered to best practices, followed the project's coding style, and addressed any potential issues.

3. **Version Control**: Git was used for version control. Each developer created a branch for their feature or bug fix, and merged their changes into the main branch after code review.

4. **Continuous Integration**: A continuous integration (CI) pipeline was set up to automatically build and test the code whenever changes were pushed to the main branch. This helped catch any issues early in the development process.

5. **Documentation**: The project's documentation, including code comments, README files, and user guides, was updated regularly to reflect the latest changes and provide clear instructions for future development and maintenance.

## Getting Started
To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/Gladwelchelangat/fitness-and-nutrition-website.git
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the database:
   - Create a new SQLite database file:
     ```
     touch app.db
     ```
   - Initialize the database:
     ```
     flask db init
     flask db migrate
     flask db upgrade
     ```

6. Run the application:
   ```
   flask run
   ```

Now you can access the website at http://localhost:5000.


