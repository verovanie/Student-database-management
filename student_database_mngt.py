from tkinter import *
from tkinter import messagebox
import backEnd_studentDatabase 

#================================= Function ========================================#

def verifier():
    a=b=c=d=e=f=l=b1=g=i=0
    if not first_name.get():
        t1.insert(END,"<>First name is required<>\n")
        a=1
    if not last_name.get():
        t1.insert(END,"<>Last name is required<>\n")
        l=1
    if not dob.get():
        t1.insert(END,"<>DoB is required<>\n")
        b=1
    if not ID.get():
        t1.insert(END,"<>ID is required<>\n")
        i=1
    if not branch.get():
        t1.insert(END,"<>Branch is required<>\n")
        b1=1
    if not gender.get():
        t1.insert(END,"<>Gender is required<>\n")
        g=1
    if not contact.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not father.get():
        t1.insert(END,"<>Father name is required<>\n")
        e=1
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or l==1 or b1==1 or g==1 or \
        i ==1:
            return 1
    else:
        return 0

def add_student() :
    global first_name,last_name,dob,ID , gender ,branch , contact ,father ,address 
    ret = verifier()
    if ret == 0:
        con = backEnd_studentDatabase.connection()
        backEnd_studentDatabase.addStudentRec(ID.get() ,first_name.get(),last_name.get(),dob.get(),branch.get() , gender.get() , father.get() ,address.get() ,contact.get())
        con.commit()
        con.close()
    t1.insert(END,"ADDED SUCCESSFULLY\n")

def search_student() :
    global first_name,last_name,dob,ID , gender ,branch , contact ,father ,address 
    ret = verifier()
    if ret==0:
        con = backEnd_studentDatabase.connection()
        a = backEnd_studentDatabase.searchData(ID.get() ,first_name.get(),last_name.get(),dob.get(),branch.get() , gender.get() , father.get() ,address.get() ,contact.get())
        print(a)
        con.commit()
        con.close()


def view_student():
    conn = backEnd_studentDatabase.connection()
    data = backEnd_studentDatabase.viewData()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")        


def delete_student() :
    global ID 
    ret = verifier()
    if ret == 0:
        con = backEnd_studentDatabase.connection()
        backEnd_studentDatabase.deleteRec(ID.get() )
        con.commit()
        con.close()

def update_student() :
    global first_name,last_name,dob,ID , gender ,branch , contact ,father ,address
    ret=verifier()
    
    if ret==0:
        con = backEnd_studentDatabase.connection()
        backEnd_studentDatabase.updateData(ID.get() ,first_name.get(),last_name.get(),dob.get(),branch.get() , gender.get() , father.get() ,address.get() ,contact.get())
        con.commit()
        con.close()

def iExit() :
    iExit = messagebox.askyesno("Student Management System" , "DO YOU WANT TO EXIT ?")
    if iExit > 0 :
        root.destroy()
        return

def clear() :
    e1.delete(0 , END)
    e2.delete(0 , END)
    e3.delete(0 , END)
    e4.delete(0 , END)
    e5.delete(0 , END)
    e6.delete(0 , END)
    e7.delete(0 , END)
    e8.delete(0 , END)
    e9.delete(0 , END)
                    
   
   


root = Tk()
root.title("Student Management System")

backEnd_studentDatabase.studentData()
#================================= Variables ========================================#

first_name = StringVar()
last_name = StringVar()
dob = StringVar()
ID = StringVar()
gender = StringVar()
branch = StringVar()
contact = StringVar()
father = StringVar()
address = StringVar()

#================================= Text Widgets ========================================#    

t1=Text(root,width=80,height=20)
t1.grid(row=10,column=1)
   
#================================= Labels ========================================#

label1 = Label(root , text = "First name :")
label1.place(x = 0 , y = 0)

label2 = Label(root , text = "Last name :")
label2.place(x = 0 , y = 30)
 
label3 = Label(root , text = "Date of Birth :")
label3.place(x = 0 , y = 60)

label11 = Label(root , text = "(DD/MM/YYYY)")
label11.place(x = 0 , y = 80)

label4 = Label(root , text = "ID :")
label4.place(x = 0,y = 100)

label5 = Label(root , text = "Gender :")
label5.place(x = 0 , y = 125)

label6 = Label(root , text = "Branch :")
label6.place(x = 0 , y = 155)

label7 = Label(root , text = "Father Name :")
label7.place(x = 0 , y = 185)

label8 = Label(root , text = "Phone Number :")
label8.place(x = 0 , y = 215)
 
label9 = Label(root , text = "Address :")
label9.place(x = 0, y = 245)

#================================= Entries ========================================#

e1 = Entry(root , textvariable = first_name)
e1.place(x = 100 , y = 0)

e2 = Entry(root , textvariable = last_name)
e2.place(x = 100 , y = 30)

e3 = Entry(root , textvariable = dob)
e3.place(x = 100 , y = 60)

e4 = Entry(root , textvariable = ID)
e4.place(x = 100 , y = 100)

e5 = Entry(root , textvariable = gender)
e5.place(x = 100 , y = 125)

e6 = Entry(root , textvariable = branch)
e6.place(x = 100 , y = 155)

e7 = Entry(root , textvariable = father)
e7.place(x = 100 , y = 185)

e8 = Entry(root , textvariable = contact)
e8.place(x = 100 , y = 215)

e9 = Entry(root , textvariable = address)
e9.place(x = 100 , y = 245)

#================================= Buttons ========================================#
b1 = Button(root , text = "ADD STUDENT" , command = add_student , width = 40)
b1.grid(row = 11 , column = 0)

b2 = Button(root , text = "SEARCH" , command = search_student , width = 40)
b2.grid(row = 12 , column = 0)

b3 = Button(root , text = "CLEAR" , command = clear , width = 40)
b3.grid(row = 13 , column = 0)

b4 = Button(root , text = "VIEW ALL STUDENTS" ,command = view_student , width = 40)
b4.grid(row = 14 , column = 0)

b5 = Button(root , text = "DELETE STUDENT" , command = delete_student , width = 40)
b5.grid(row = 15 , column = 0)

b6 = Button(root , text = "UPDATE INFO" , command = update_student , width = 40)
b6.grid(row = 16, column = 0)

b7 = Button(root , text = "CLOSE" ,command = iExit , width = 40)
b7.grid(row = 17 , column = 0)


root.mainloop()


