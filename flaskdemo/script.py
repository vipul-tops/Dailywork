from flask import Flask,render_template,request

app = Flask("__main__")

@app.route("/index/<int:num>")
def index(num):
    return render_template('index.html',num=num)

@app.route("/querydemo")
def querydemo():
    return render_template('querydemo.html')
    print(request.args)
    return "Request Query"

@app.route("/filter_demo")
def filter_demo():
    names = ['Vipul', 'Aksh', 'Jinal', 'Sanjay']
    age = [25, 21, 9, 28 ]
    return render_template('filter_demo.html',context={'names':names,'age':age} )


app.run(debug=True)