from flask import Flask  , redirect ,url_for , request

app = Flask(__name__)  
  
  
@app.route('/login',methods = ['GET'])  
def login():  
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="nikola" and passwrd=="123456":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True) 