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

@app.route("/form",methods=['GET','POST'])
def formm():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route("/submit",methods=['GET','POST'])
def suuuubmit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

if __name__ == "___main__":
    app.run(debug=True)