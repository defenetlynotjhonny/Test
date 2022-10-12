from flask import Flask  , redirect ,url_for 


app = Flask(__name__)  
  
@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="nikola" and passwrd=="123456":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)