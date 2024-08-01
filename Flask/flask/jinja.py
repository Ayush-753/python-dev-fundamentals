### Build URL Dynamically
## Variable Rule
### JINJA2 template engine

from flask import Flask, render_template, request

###WSGI Application
app=Flask(__name__) # It creates instance of flask class, which will be your WSGI (Web Server Gateway Interface) application.

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask demo</H1><html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/submit",methods=['GET','POST'])
def suuuubmit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

## Variable Rule
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score>=50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', results=res)
   # return "The marks you got is "+ str(score)

if __name__ == "___main__":     # entry point of the application
    app.run(debug=True)