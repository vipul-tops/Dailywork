from flask import Flask, url_for

app = Flask("__main__")

@app.route("/")
def inde():
    msg = "Hello Wolrd !!"
    return msg

@app.route("/blog")
def blog():
    msg = "This Is Blog PAge"
    return msg

@app.route("/home")
@app.route("/home/<username>")
def home(username='Guest'):
    return "Welcome to Home Page of " + username

@app.route("/blog/<int:blog_no>")
def get_blog(blog_no):
    return "This is Blog Number : " + str(blog_no)

@app.route("/check/<int:number>")
def check(number):
    if number % 2 ==0:
        return "This is <b> Even </b>"
    return "This Is <b> ODD </b>"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('home',username='Vipul Memakiya'))
    print(url_for('home',username='Vishal',password='123'))

app.run(debug=True)