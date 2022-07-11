from flask import Flask, render_template, request
import os
import smtplib

# Configuration

app = Flask(__name__)

char_per_line = 5
# Routes 

open_bio = open('./static/text/bio.txt','r')
bio = open_bio.read()

open_resume = open('./static/text/resume.txt','r')
resume = open_resume.read()

@app.route('/')
def root():
    return render_template("home.j2", bio=bio, resume=resume)

@app.route('/email', methods=["POST"])
def email():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login("milldevo@oregonstate.edu", "Gunsnrosespatriots12")
    server.sendmail("milldevo@oregonstate.edu", email, message)

    if not first_name or not last_name or not email:
        error_message = "All fields required"
        return render_template("home.j2",
        error_statement=error_message,
        first_name=first_name,
        last_name=last_name,
        email=email)
    
    alert("attempt succesful")
    return render_template("home.j2")





if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port)