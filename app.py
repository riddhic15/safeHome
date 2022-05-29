from email import encoders
from email.mime import image
from flask import Flask, render_template, Response, request, flash
from flask_mail import *
import smtplib
from email.mime.image import MIMEImage
import cv2
import os
import time
from faceDetect import facedetection
from recognition import recog
from inputs import names, recognize, train_finally, append_list
import sys
import inputs
from training import train_the_model

app = Flask(__name__)
app.secret_key = "super secret key" 

prev_time = 0

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_ASCII_ATTACHMENTS'] = False
mail = Mail(app)

# to_addr = input('To: ')

@app.route('/send_email')
def send_email(img_name):
    with app.app_context():
        msg = Message('ALERT!', sender =   'safeHome.official@gmail.com', recipients = ['riddhichaudhary15@gmail.com'])
        msg.body = "Dear customer, \n\n We have noticed unknown people at your home. Kindly, take action if you do not recognise this activity.\n Attached with this mail is a snapshot of the unrecognised person at your home.\n\n Regards, \n safeHome"
        try:
            with app.open_resource(img_name) as fp:
                msg.attach(filename= img_name, content_type="image/jpg", data=fp.read())
                mail.send(msg)
        except Exception as e:
            print(e)
        return "Message sent"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homemode')
def home():
    return render_template('home.html')

@app.route('/awaymode')
def away():
    return render_template('away.html')

@app.route('/recognized')
def recognized():
    return render_template('recognized.html', recognized=names)

@app.route('/add',  methods=["GET", "POST"])
def add():
    if request.method == "POST":
        newname = request.form.get('name')
        append_list(newname)
        train_finally()
        flashmessage = f"Added {newname} as a member successfully!"
        flash(flashmessage)
    return render_template('add.html')

@app.route('/video_feed_train')
def video_feed_train():
    global prev_time
    return Response (facedetection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_recog')
def video_feed_recog():
    if len(names) == 1:
        return Response (facedetection(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return Response (recognize(), mimetype='multipart/x-mixed-replace; boundary=frame')
        
    

@app.route('/video_feed_facedetect')
def video_feed_facedetect():
    return Response (facedetection(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)