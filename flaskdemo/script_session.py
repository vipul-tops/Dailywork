from flask import Flask,request,render_template,session,redirect,url_for

app = Flask("__name__")
app.secret_key = 'a@34s4f#5%'

@app.route("/login", methods = ['GET','POST'])
def login():
    if request.method == "POST":
        session['uname'] = request.form.get('username')
        return render_template('profile.html')
    
    if 'uname' in session:
        return "You Have Already Registered"
    
    return '''<form method = 'post' action='/login' >
            <p><h3>Enter Name </h3></p>
            <input type="text" name="username"/>
            <p> <input type='submit' value='Go'/></p>
            </form>'''

@app.route("/profile")
def profile():
    #uname = session['uname']
    uname = session.get('uname')
    if uname == None :
        return redirect(url_for('login'))
    return "Welcome {}".format(uname)

@app.route("/logout")
def logout():
    session.pop('uname')
    return "You Are Successfully Logout !!!!"

app.run(debug=True)