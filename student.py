from tkinter import * #importing tkinter modules
from tkinter import ttk # ttk module provide access to the Tk themed widget set
import tkinter.messagebox # to pop-up the message box
import pymysql # to connect the mysql server
import mysql.connector

class ConnectorDB:
    def __init__(self,root):
        self.root = root
        titlespace = " " # a variable with space as value
        self.root.title(110*titlespace+"CRUD Student") # to bring the title in middle
        self.root.geometry("759x637+300+0") # to give size of application
        self.root.resizable(width=False,height=False) # to fix the size of application

#"""--------------------------------Creating Frame--------------------------------"""

        MainFrame = Frame(self.root, bd=10,width=770,height=700,relief=RIDGE,bg='red') #to give color to application, bd=border,bg= background
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,bd=7,width=770,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)
        TopFrame3 = Frame(MainFrame,bd=5,width=770,height=500,relief=RIDGE)
        TopFrame3.grid(row=1,column=0)

        LeftFrame = Frame(TopFrame3,bd=5,width=770,height=400,padx=2,bg='red',relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame,bd=5,width=600,height=180,padx=12,pady=9,relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3,bd=5,width=100,height=400,padx=2,bg='red',relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1,bd=5,width=90,height=300,padx=2,pady=2,relief=RIDGE)
        RightFrame1a.pack(side=TOP)

#"""--------------------------------------------------------------------------------------------"""
        StudentID = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()
#===============================================All Functions=======================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("CRUD Student","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
                self.entStudentID.delete(0,END)
                self.entFirstName.delete(0,END)
                self.entLastName.delete(0,END)
                self.entAddress.delete(0,END)
                self.entMobile.delete(0,END)
                Gender.set("Male")

        def addData():
                if StudentID.get() == "" or FirstName.get() =="" or LastName.get()=="" or Mobile.get()=="":
                        tkinter.messagebox.showerror("CRUD Student","Enter the Correct Details")
                else:
                        mydb = mysql.connector.connect(host="localhost", user="root",password="",database="crud_student")
                        connect = mydb.cursor()
                        connect.execute("Insert into studentsinfo value(%s,%s,%s,%s,%s,%s)",(
                                StudentID.get(),
                                FirstName.get(),
                                LastName.get(),
                                Gender.get(),
                                Address.get(),
                                Mobile.get(), 
                        ))
                        mydb.commit()
                        mydb.close()
                        tkinter.messagebox.showinfo("CRUD Student","Data saved successfully")
        
        def DisplayData():
                mydb = mysql.connector.connect(host="localhost", user="root",password="",database="crud_student")
                connect = mydb.cursor()
                connect.execute("select * from studentsinfo")
                result = connect.fetchall()
                if len(result)!=0:
                        self.student_records.delete(*self.student_records.get_children())
                        for row in result:
                                self.student_records.insert('',END,values=row)
                mydb.commit()
                mydb.close()
                #tkinter.messagebox.showinfo("CRUD Student","Data saved successfully")
                
        def StudentInfo(ev):# when we click on details then the information will be fetched into input fields 
                viewInfo = self.student_records.focus()
                learnerData = self.student_records.item(viewInfo)
                row = learnerData['values']
                StudentID.set(row[0])
                FirstName.set(row[1])
                LastName.set(row[2])
                Gender.set(row[3])
                Address.set(row[4])
                Mobile.set(row[5])

        def update():
                mydb = mysql.connector.connect(host="localhost", user="root",password="",database="crud_student")
                connect = mydb.cursor()
                connect.execute("Update studentsinfo set firstname=%s,lastname=%s,gender=%s,address=%s,mobile=%s where stdid=%s",(
                                
                                FirstName.get(),
                                LastName.get(),
                                Gender.get(),
                                Address.get(),
                                Mobile.get(),
                                StudentID.get()
                        ))
                mydb.commit()
                mydb.close()
                tkinter.messagebox.showinfo("CRUD Student","Data Updated successfully")

        def delete():
                mydb = mysql.connector.connect(host="localhost", user="root",password="",database="crud_student")
                connect = mydb.cursor()
                connect.execute("delete from studentsinfo where stdid=%s"%StudentID.get())
                mydb.commit()
                DisplayData()
                mydb.close()
                tkinter.messagebox.showinfo("CRUD Student","Data deleted successfully")
                Reset()

        def search():
                try:
                        mydb = mysql.connector.connect(host="localhost", user="root",password="",database="crud_student")
                        connect = mydb.cursor()
                        connect.execute("select * from studentsinfo where stdid=%s"%StudentID.get())
                        row = connect.fetchone()

                        StudentID.set(row[0])
                        FirstName.set(row[1])
                        LastName.set(row[2])
                        Gender.set(row[3])
                        Address.set(row[4])
                        Mobile.set(row[5])

                        mydb.commit()
                except:
                        #mydb.rollback()
                        tkinter.messagebox.showinfo("CRUD Student","No Such record found")
                        Reset()
                mydb.close()
#======================================================================================================

        self.lbltitle = Label(TitleFrame,font=('arial',40,'bold'),text="Manage Student",bd=7,fg='red')
        self.lbltitle.grid(row=0,column=0,padx=132)

        self.lblstudentID = Label(LeftFrame1, font=('arial',12,'bold'),text="Student ID",bd=7,fg='red')
        self.lblstudentID.grid(row=1,column=0,sticky=W,padx=5)
        self.entStudentID = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=StudentID)
        self.entStudentID.grid(row=1,column=1,sticky=W,padx=5)

        self.lblFirstName = Label(LeftFrame1, font=('arial',12,'bold'),text="FirstName",bd=7,fg='red')
        self.lblFirstName.grid(row=2,column=0,sticky=W,padx=5)
        self.entFirstName = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=FirstName)
        self.entFirstName.grid(row=2,column=1,sticky=W,padx=5)

        self.lblLastName = Label(LeftFrame1, font=('arial',12,'bold'),text="LastName",bd=7,fg='red')
        self.lblLastName.grid(row=3,column=0,sticky=W,padx=5)
        self.entLastName = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=LastName)
        self.entLastName.grid(row=3,column=1,sticky=W,padx=5)

        self.lblAddress = Label(LeftFrame1, font=('arial',12,'bold'),text="Address",bd=7,fg='red')
        self.lblAddress.grid(row=4,column=0,sticky=W,padx=5)
        self.entAddress = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=Address)
        self.entAddress.grid(row=4,column=1,sticky=W,padx=5)

        self.lblGender = Label(LeftFrame1, font=('arial',12,'bold'),text="Gender",bd=7,fg='red')
        self.lblGender.grid(row=5,column=0,sticky=W,padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=43,state='readonly',textvariable=Gender)
        self.cboGender['values']=('Male','Female','Trans')
        self.cboGender.current(0)
        self.cboGender.grid(row=5,column=1,sticky=W,padx=5)

        self.lblMobile = Label(LeftFrame1, font=('arial',12,'bold'),text="Mobile",bd=7,fg='red')
        self.lblMobile.grid(row=6,column=0,sticky=W,padx=5)
        self.entMobile = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=Mobile)
        self.entMobile.grid(row=6,column=1,sticky=W,padx=5)

#====================================Table TreeView =======================================
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)

        self.student_records = ttk.Treeview(LeftFrame,height=12,columns=("stdid","firstname","lastname","gender","address","mobile"),yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT,fill=Y)

        self.student_records.heading("stdid",text="StudentID")
        self.student_records.heading("firstname",text="FirstName")
        self.student_records.heading("lastname",text="LastName")
        self.student_records.heading("address",text="Address")
        self.student_records.heading("gender",text="Gender")
        self.student_records.heading("mobile",text="Mobile")

        self.student_records['show']='headings'

        self.student_records.column("stdid",width=70)
        self.student_records.column("firstname",width=100)
        self.student_records.column("lastname",width=100)
        self.student_records.column("address",width=100)
        self.student_records.column("gender",width=70)
        self.student_records.column("mobile",width=70)

        self.student_records.pack(fill=BOTH,expand=1)
        self.student_records.bind("<ButtonRelease-1>",StudentInfo) # when we click on details then the information will be fetched into input fields
        DisplayData() #comment it if you want display data using clicking button of Display

#===================================Buttons=============================================
        self.btnAddNew = Button(RightFrame1a,font=('arial',16,'bold'),fg='red',text="Add New",bd=4,pady=1,padx=24,width=5,height=2,command=addData).grid(row=0,column=0,padx=1)

        self.btndisplay = Button(RightFrame1a,font=('arial',16,'bold'),fg='red',text="Refresh",bd=4,pady=1,padx=24,width=5,height=2,command=DisplayData).grid(row=1,column=0,padx=1)
        
        self.btndelete = Button(RightFrame1a,font=('arial',16,'bold'),fg='red',text="Delete",bd=4,pady=1,padx=24,width=5,height=2,command=delete).grid(row=2,column=0,padx=1)

        self.btnupdate = Button(RightFrame1a,font=('arial',16,'bold'),fg='red',text="Update",bd=4,pady=1,padx=24,width=5,height=2,command=update).grid(row=3,column=0,padx=1)

        self.btnsearch = Button(RightFrame1a,font=('arial',16,'bold'),fg='red',text="Search",bd=4,pady=1,padx=24,width=5,height=2,command=search).grid(row=4,column=0,padx=1)

        self.btnreset = Button(RightFrame1a,font=('arial',16,'bold'),fg='red',text="Reset",bd=4,pady=1,padx=24,width=5,height=2,command=Reset).grid(row=5,column=0,padx=1)

        self.btnexit = Button(RightFrame1a,font=('arial',16,'bold'),fg='red',text="Exit",bd=4,pady=1,padx=24,width=5,height=2,command=iExit).grid(row=6,column=0,padx=1)
#================================================================================
        


if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop() 