import sqlite3

def connection():
    try:
        conn=sqlite3.connect("student.db")
    except:
        print("cannot connect to the database")
    return conn

def studentData() :
    con = connection()
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS student(
        ID TEXT PRIMARY KEY , 
        Firstname TEXT , 
        Surname TEXT ,
        DoB TEXT , 
        Gender TEXT , 
        Branch TEXT , 
        Father TEXT ,
        Address TEXT ,
        Mobile INTEGER)''')
    
    con.commit()
    con.close()
    
            
            
def addStudentRec(ID , Firstname , Surname , DoB, Branch , Gender ,Father ,Address ,Mobile) :
    con = connection()
    con = sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("INSERT INTO student VALUES(?,?,?,?,?,?,?,?,?)",(ID , Firstname , Surname , DoB, Branch , Gender ,Father ,Address ,int(Mobile)))
    con.commit()
    con.close()
    
def viewData() :
    con = connection()
    con = sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM student ") 
    row = cur.fetchall()
    con.close()
    return row

def deleteRec(ID) :
    con = connection()
    con = sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("DELETE FROM student WHERE id = ? " , (ID)) 
    con.commit()
    con.close()
    
def searchData(ID = "" , Firstname = "" , Surname = "" , DoB = "" , Branch = "" ,\
               Gender = "" , Father =""  ,Address = "" ,Mobile = "" ) :
    con = connection()
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE ID = ? , Firstname = ? , \
                Surname = ? , DoB = ? ,Branch = ? , Gender = ? ,Father = ? , Address = ? ,Mobile = ? ",\
                (ID , Firstname , Surname , DoB, Branch , Gender ,Father ,Address ,Mobile)) 
    row = cur.fetchall()
    con.close()
    return row

def updateData(ID  , Firstname = "" , Surname = "" , DoB = "" , Branch = "",\
               Gender = "" , Father =""  ,Address = "" ,Mobile = "" ) :
    con = connection()
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student WHERE ID = ? , Firstname = ? , \
                Surname = ? , DoB = ? ,Branch = ? , Gender = ? ,Father = ? ,\
                Address = ? ,Mobile = ? " , ( Firstname , Surname , DoB, Branch ,\
                Gender ,Father ,Address ,Mobile ,ID)) 
    con.close()

    
    

    
studentData()
