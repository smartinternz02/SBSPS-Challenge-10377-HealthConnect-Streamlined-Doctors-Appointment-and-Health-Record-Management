# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
def showall():
    sql= "SELECT * from USER"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["Name"])
        print("The E-mail is : ", dictionary["Email"])
        print("The Password is : ",  dictionary["Password"])
        print("The Confirm Password is : ", dictionary["ConfirmPassword"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(Email,Password):
    sql= "select * from USER where Email='{}' and Password='{}'".format(Email,Password)
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

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=trj84841;PWD=W7xnyTpsO92ICmTQ",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"Hari","Hari@gmail.com",'1234567890','Adarsh nagar','Faculty','Civil','1234567')
    getdetails("Hari@gmail.com",'1234567')
    #showall()

except:
    print("Error connecting to the database")



