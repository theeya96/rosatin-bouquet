from flask import Flask #the module(flask), import class=Flask

app = Flask(__name__) #Create an app(object of the class Flask). Everytime create flask app need a name. 

@app.route("/") #Telling flask that when certain url is requested, what should be returned (Eg. jovien.ai/askashns or jovien/learn))

def hello_world(): #Defining a fuction 
  return "Hello!" #Returns string Hello World

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)

