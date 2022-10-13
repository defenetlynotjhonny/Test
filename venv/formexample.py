from flask import Flask, render_template, request, flash  
from forms import ContactForm
from flask_wtf import Form

app = Flask(__name__)  
app.secret_key ='development key'



@app.route('/')  
def index():  
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def hello():
    return render_template("login.html")

@app.route('/contact', methods = ['GET'])  
def contact():  
   form = ContactForm()  
   if form.validate() == False:  
      flash('All fields are required.')  
   return render_template('contact.html', form = form)  
  
@app.route('/Customer', methods = ['GET'])
def customer():
   return render_template('customer.html')


@app.route('/file_upload_form', methods = ['GET'])
def file_upload_form():
   return render_template('file_upload_form.html')
  
@app.route('/Logout', methods = ['GET'])
def Logout():
   return render_template('logout.html')

@app.route('/message', methods = ['GET'])
def message():
   return render_template('message.html')

@app.route('/profile', methods = ['GET'])
def profile():
   return render_template('profile.html')  

@app.route('/result_data', methods = ['GET'])
def result_data():
   return render_template('result_dat.html')

@app.route('/success',methods = ['GET','POST'])  
def success():  
   return render_template("success.html") 

 

 
  
if __name__ == '__main__':  
   app.run(debug = True)  