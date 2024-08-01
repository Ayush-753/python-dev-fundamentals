from flask import Flask, render_template

###WSGI Application
app=Flask(__name__) # It creates instance of flask class, which will be your WSGI (Web Server Gateway Interface) application.

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask demo</H1><html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "___main__":     # entry point of the application
    app.run(debug=True)