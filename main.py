from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")

database={'Test@gmail.com':'123','admin@dut4life.co.za':'admin','22041263@dut4life.co.za':'Dut@1208'}

@app.route('/Admin',methods=['POST','GET'])
def admin():
    """Renders the contact page."""
    return render_template(
        'Admin.html',
        title='Contact',
        message='Your contact page.'
    )
@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']

    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('home.html',name=name1)


if __name__ == '__main__':
    app.run()
