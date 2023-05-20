from flask import Flask  #predefined class Flask
a = Flask(__name__) #constructor  , object for the class

@a.route("/") # / - default rout 
def home():
    return "welcome to my first page"
# a.run()

@a.route("/login") # / - default rout 
def login():
    return "This is Login page"
# a.run()

@a.route("/<name>") # / - default rout 
def namepage(name):
    return "Hii....This is {} !".format(name)
a.run()