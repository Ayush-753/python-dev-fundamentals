### Build URL Dynamically
## Variable Rule
### JINJA2 template engine

### JINJA2 template engine
'''
{{}} expressions to print output in html
{%....%} conditions, for loops
{#....#} used for comments

'''

from flask import Flask, render_template, request, redirect, url_for

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

'''@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
'''
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

## if condition
@app.route("/successif/<int:score>")
def sucif(score):
    
    return render_template('result.html', results=score)
 
 
@app.route("/fail/<int:score>")
def fail(score):
    
    return render_template('result.html', results=res)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres',score=total_score))
        
    
  
if __name__ == "___main__":
    app.run(debug=True)