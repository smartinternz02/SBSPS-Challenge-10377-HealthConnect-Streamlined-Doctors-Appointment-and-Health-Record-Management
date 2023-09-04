from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
def showall():
    sql= "SELECT * from USER"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["Name"])
        print("The E-mail is : ", dictionary["Email"])
        print("The Password is : ",  dictionary["Password"])
        print("The ConfirmPassword is : ",  dictionary["ConfirmPassword"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(Email,Password):
    sql= "select * from USER where email='{}' and password='{}'".format(Email,Password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["Name"])
        print("The E-mail is : ", dictionary["Email"])
        print("The Password is : ", dictionary["Password"])
        print("The Confirm Password is : ", dictionary["ConfirmPassword"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(Name,Email,Password,ConfirmPassword):
    sql= "INSERT into USER VALUES('{}','{}','{}','{}')".format(Name,Email,Password,ConfirmPassword)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=trj84841;PWD=W7xnyTpsO92ICmTQ",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/SignUp', methods=['POST','GET'])
def register():
    if request.method == "POST":
        Name = request.form['Name']
        Email = request.form['Email']
        Password = request.form['Password']
        ConfirmPassword = request.form['ConfirmPassword']
        
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(Name,Email,Password,ConfirmPassword)
        return render_template('login.html')
        

@app.route('/login', methods=['POST','GET'])
def signin():
    if request.method == "POST":
        Email = request.form['Email']
        Password = request.form['Password']
        sql= "select * from USER where Email='{}' and Password='{}'".format(Email,Password)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['register'] =userdetails["Email"]
            return render_template('userprofile.html',Email= userdetails["Email"],Password=userdetails["Password"])
        else:
            msg = "Incorrect Email id or Password"
            return render_template("login.html", msg=msg)
    return render_template('index.html')


if __name__ =='__main__':
    app.run( debug = True)
