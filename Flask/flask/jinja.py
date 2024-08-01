### Build URL Dynamically
## Variable Rule
### JINJA2 template engine

### JINJA2 template engine
'''
{{}} expressions to print output in html
{%....%} conditions, for loops
{#....#} used for comments

'''

from flask import Flask, render_template, request

app=Flask(__name__)

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
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html', results=res)
   # return "The marks you got is "+ str(score)

## Variable Rule
@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
        
    exp={'score':score, "res":res}
        
    return render_template('result1.html', results=exp)

if __name__ == "___main__":
    app.run(debug=True)