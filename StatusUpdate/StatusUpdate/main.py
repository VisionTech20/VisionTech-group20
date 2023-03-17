import mail
from flask import Flask, render_template, request, app
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/complaints/<int:id>/update', methods=['GET', 'POST'])
def update_complaint():
    if request.method == 'POST':
        status = request.form['status']

        # here we will code to update the status of the complaint in the database

        # looks the email from your database based on the complaint id
        email = 'user@example.com'

        message = Message('Complaint status update', sender='your-email@gmail.com', recipients=[email])
        message.body = f"Dear {email},\n\nYour complaint has been received and the issue is being resolved"
        mail.send(message)

        return render_template('update.html')
