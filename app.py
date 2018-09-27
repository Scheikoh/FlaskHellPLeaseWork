from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/index2')
def index2():
    return render_template('index2.html')


#  importing pymysql
import pymysql
from flask import request
@app.route('/blog', methods=['POST','GET'])
def blog():
    #  Logic goes here
    if request.method=='POST': #  Check if user posted
        email = request.form['email']
        name = request.form['name']
        msg = request.form['msg']

        #  saving to db
        #  establish db connection
        con = pymysql.connect("localhost", "root", "", "janet_db")
        #  execute mysql
        #  Create a cursor object
        cursor = con.cursor()
        # %s for avoiding sql hack, data passed later
        sql = "INSERT INTO `messages_tbl`( `name`, `email`, `msg`) VALUES (%s,%s,%s)"
        cursor.execute(sql, (name, email, msg))
        con.commit()   # Saves changes to db

        return render_template('blog.html')
    else:
        return render_template('blog.html')


if __name__ == '__main__':
    app.run()
