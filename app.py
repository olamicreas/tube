import phonenumbers
from flask import Flask, render_template, request, flash, redirect, url_for, session, abort, jsonify, send_file
import urllib.request
from forms import Track
from pytube import YouTube
from io import BytesIO
from uuid import uuid4
import random, string
from downloader import URLOpenResult, Downloader
from datetime import datetime
from flask_mail import Mail, Message
from bs4 import BeautifulSoup
from  phonenumbers import geocoder, timezone, carrier
import datetime
import os, secrets
import time
import json
import pickle
import requests
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

mail = Mail(app)
 





app.config["DEBUG"] = True


app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'olamicreas@gmail.com'
app.config['MAIL_PASSWORD'] = 'rwqdpqnsosdahvjf'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'olamicreas@gmail.com'
mail = Mail(app)



@app.route('/', methods=['POST', 'GET'])
def t():
    
    form = Track(request.form)
    d = request.form.get('d')
    
    if request.method == 'POST':
        try:
            
            download_path = YouTube(d).streams.get_highest_resolution().download()
            
            fname = download_path.split("//")[-1]
               
            return send_file(fname, as_attachment=True)
                        

            
            
        except Exception as e:
            flash("Error Downloading", 'danger')
            print(e)
        
    
    return render_template('tube.html', title='Tube Downloader')
@app.route('/privacy')
def privacy():
    return render_template('privacy.html', title='privacy')

@app.route('/terms-service')
def terms():
    return render_template('terms.html', title='terms & service')

@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == "__main__":
    app.run()
