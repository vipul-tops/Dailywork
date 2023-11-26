from flask import Flask,render_template,request,make_response
import requests

app = Flask("__main__")

@app.route("/index/<int:num>")
def index(num):
    return render_template('index.html',num=num)

@app.route("/querydemo")
def querydemo():
    return render_template('querydemo.html')
    # print(request.args)
    # return "Request Query"

@app.route("/takedata")
def takedata():
    return render_template('takedata.html')

@app.route("/fetchdata",methods=['POST'])
def fetchdata():
    print(request.form)
    return "<h2> the Name Is {} and The Number is {} </h2>".format(request.form.get('name'),request.form.get('number'))
    # return render_template('fetchdata.html')

@app.route("/filter_demo")
def filter_demo():
    names = ['Vipul', 'Aksh', 'Jinal', 'Sanjay']
    age = [25, 21, 9, 28 ]
    return render_template('filter_demo.html',context={'names':names,'age':age} )

@app.route("/makejson")
def makejson():
    person = {
        "name" : "Vipul",
        "language" : "Python",
        "framework" : ["Flask","Django"]
    }
    res = requests.post("http://127.0.0.1:5000/processJson",json=person)
    return res.text

@app.route("/processJson",methods=['post'])
def process_json():
    if request.is_json:
        return request.json
        # return request.json.get('name')
    else:
        return " It has Not Any Json Data"

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        res = make_response(render_template('get_profile.html'))
        res.set_cookie("userID",request.form.get('username'))
        return res
    
    return '''<form method = 'post' action='/login' >
            <p><h3>Enter Name </h3></p>
            <input type="text" name="username"/>
            <p> <input type='submit' value='Go'/></p>
            </form>'''

@app.route("/getProfile")
def get_profile():
    name = request.cookies.get('userID')
    if name == None:
        name = "Guest"
    return "Welcome {}".format (name)

@app.route("/logout")
def logout():
    res = make_response(render_template('get_profile.html'))
    res.delete_cookie('userID')
    return res

app.run(debug=True)