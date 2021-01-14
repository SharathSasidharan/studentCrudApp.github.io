from tkinter import *      #imported tkinter file
from tkinter import ttk    # this imported because it provides  combo boxes used in gender functionalitty
import pymysql             # used for large amount of data
import re                  # re to work with RegEx
from tkinter import messagebox  # MessageBox Widget is used to display the message boxes in the python applications
from validate_email import validate_email  #Validate_email is a package for Python that check if an email is valid, properly formatted and really exists.
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib import colors
# from bleach._vendor.html5lib._i
# import pyodbc
import os
import csv

class Student:
    # we have to Initialize the constructor
    def __init__(self,root):
       #first need to initalize the root
        self.root=root
        # Giving Title to the window
        self.root.title("Student Management System ")
        # width x height + x position + y position, positions relative to the top left corner of the screen in pixels
        self.root.geometry("1350x700+0+0")    

         
        # now to create the frames ie.Title, left-side: student management frame , right-side: details frame  
        # first need to showcase the title in Top section in self.root window 
        # intialize a label here over here with the label object and passing in parameter  
        # first argument i.e. self.root : that's the label is going to be associated with 
        # bd =10: border-width used around the widgets 
        # relief=GROOVE: relief is assigned groove its just a border style groove around the text
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg="grey",fg="black")
        # pack() function helps us to place objects in different locations of our window 
        # side attribute where to pack used TOP 
        # fill=X : fill only horizontally it will take the full-width size according to its window 
        title.pack(side=TOP,fill=X)

       
          #***** WE MAKE SOME VARIABLES TO START WITH THE DATABASE**********
          # Used StringVar() for roll no and contact because not performing calculations
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        
         #search by name on right-panel=>
        self.search_by=StringVar()
        self.search_txt=StringVar()  









        #--------------------WORKING ON LEFT PANEL----------------------#

        # Frame: It acts as a container to hold the widgets. It is used for grouping and organizing the widgets 
      
        left_panel=Frame(self.root,bd=4,relief=RIDGE,bg='grey')
        # place()method: It allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window
        #x, y − Horizontal and vertical offset in pixels.
        #height, width − Height and width in pixels.
        left_panel.place(x=20,y=100,width=520,height=625) 
         
        #--------------header-text--------------
        # first argument takes in label ie.left_panel because now we place text inside this instead in the window
        s_title=Label(left_panel,text="STUDENT DATA ",bg='grey',fg='black', font=('times new roman',30,'bold')) 
        # grid layout of the widgets in row and column-wise
        #row: The row to put widget in default the first row that is still empty.
        # columnspan − How many columns widgetoccupies; default 1.
        #padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders.
        s_title.grid(row=0,columnspan=2,pady=20)
         
      
        #label_rollno
        # Roll-no comes to row 1
        # property:sticky='w'to make it left side 
        lbl_roll=Label(left_panel,text="Roll No ",bg='grey',fg='black', font=('times new roman',20,'bold')) 
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky='w')  

        
        #The Entry widget is used to accept single-line text strings from a user.
        #textvar= self.rollno variables defined in entry fields
        txt_roll=Entry(left_panel,textvar=self.Roll_No_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE) 
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        lbl_name=Label(left_panel,text="Name ",bg='grey',fg='black', font=('times new roman',20,'bold')) 
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')  #property:sticky:to make it left side 
         #textvar= self.name variables defined in entry fields
        txt_name=Entry(left_panel,textvar=self.name_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE) 
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

        lbl_Email=Label(left_panel,text="E-mail ",bg='grey',fg='black', font=('times new roman',20,'bold')) 
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky='w')  #property:sticky:to make it left side 
         
        #textvar= self.email variables defined in entry fields 
        txt_Email=Entry(left_panel,textvar=self.email_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE) 
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky='w')

        lbl_Gender=Label(left_panel,text="Gender ",bg='grey',fg='black', font=('times new roman',20,'bold')) 
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')  #property:sticky:to make it left side 

        #Combo boxes
        # used one property here ie state = readonly , users will not modify to do only selects from the list
         #textvar= self.gender variables defined in entry fields
        combo_gender=ttk.Combobox(left_panel,textvar=self.gender_var,font=('times new roman',13,'bold'),state='readonly')
        # passing the tuples in values
        # Adding combobox drop down list 
        combo_gender['values'] = ('Gender','Male','Female','Others')
        combo_gender.grid(row=4,column=1,pady=10,padx=20)
        combo_gender.current(0)
 
        lbl_Contact=Label(left_panel,text="Contact ",bg='grey',fg='black', font=('times new roman',20,'bold')) 
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky='w')  #property:sticky:to make it left side 
        #textvar= self.contact variables defined in entry fields
        txt_Contact=Entry(left_panel,textvar=self.contact_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE) 
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')  
   
        
        lbl_dob=Label(left_panel,text="D.O.B ",bg='grey',fg='black', font=('times new roman',20,'bold')) 
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky='w')  #property:sticky:to make it left side 
   
        #textvar= self.dob variables defined in entry fields
        txt_dob=Entry(left_panel,textvar=self.dob_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE) 
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky='w')  
   
        lbl_address=Label(left_panel,text="Address",bg='grey',fg='black', font=('times new roman',20,'bold')) 
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky='w')
     
        # Text Widget is used where a user wants to insert multiline text fields
        # for text_address textvar attribute will be not there ,so to access the text field data we take the help of self
        self.txt_address=Text(left_panel,width=30,height=3,font=('',10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky='w')

        
        '''Now the next step is to make button so for that we need to 
           create one frame      '''
        
        btn_panel=Frame(left_panel,bd=4,relief=RIDGE,bg='grey')
        btn_panel.place(x=5,y=500,width=500) 
        
        #ADD BUTTON
        # Command is the attribute of buttons that takes in what should happen when a button is pressed so passed here button function   
        add_btn=Button(btn_panel,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        update_btn=Button(btn_panel,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete_btn=Button(btn_panel,text="Delete",width=10,command=self.Delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear_btn=Button(btn_panel,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        exit_btn=Button(btn_panel,text="Log Out",width=10,command=self.iExit).grid(row=0,column=4,padx=10,pady=10)
        pdf_gen=Button(btn_panel,text="Genrate PDF",width=10,command=self.gen_pdf).grid(row=1,column=1,padx=10,pady=10)
        export_csv=Button(btn_panel,text="Export To csv",width=10,command=self.Export).grid(row=1,column=2,padx=10,pady=10)

        
        
        
        
        #--------------------------WORKING ON RIGHT PANEL---------------
        
        right_panel=Frame(self.root,bd=4,relief=RIDGE,bg='grey')
        # place()method: It allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window
        #x, y − Horizontal and vertical offset in pixels.
        #height, width − Height and width in pixels.
        right_panel.place(x=560,y=100,width=800,height=625) 

    
         #first column will be the Search

        lbl_Search=Label(right_panel,text="Search By",bg='grey',fg='black', font=('times new roman',20,'bold')) 
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky='w')

        combo_search=ttk.Combobox(right_panel,width=10,textvar=self.search_by,font=('times new roman',13,'bold'),state='readonly')
        combo_search['values']=('Roll_no','Name','Contact')
        combo_search.grid(row=0,column=1,pady=10,padx=20)
       
        
        txt_search=Entry(right_panel,width=20,textvar=self.search_txt,font=('times new roman',10,'bold'),bd=5,relief=GROOVE) 
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')  
        

        search_btn=Button(right_panel,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        search_btn=Button(right_panel,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


       # ****************TABLE FRAME***************************#

        table_data=Frame(right_panel,bd=4,relief=RIDGE,bg='grey')
        table_data.place(x=10,y=70,width=760,height=500)
    
         
           #STUDENT Display Records
        # Scrollbar: It refers to the slide controller which will be used to implement listed widgets.
        scroll_x=Scrollbar(table_data,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_data,orient=VERTICAL)
        #TreeView widget: want to display a hierarchy of items, with all attributes listed side by side.
        #table_data refers to the tkinter application in table_data mode
        #columns is a tuple, which refers to the names of the columns
        self.student_table=ttk.Treeview(table_data,columns=('roll','name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)

        scroll_y.pack(side=RIGHT,fill=Y)
        # config is used to access an object's attributes after its initialisation
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        # STUDENT TABLE HEADING
        # defined the column above to fetch accordingly and what to show to the user ie. text here.
        self.student_table.heading('roll',text='Roll No')
        self.student_table.heading('name',text='Name')
        self.student_table.heading('email',text='E-Mail')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('contact',text='Contact')
        self.student_table.heading('dob',text='D.O.B')
        self.student_table.heading('address',text='Address')
        
        # IT WILL ELIMINATE THE UNUSED SPACES WHICH ARE ALLOTED IN TABLE HEADINGS
        self.student_table['show']='headings'
        # ADJUSTING THE WIDTH OF COLUMNS
        self.student_table.column('roll',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('contact',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('address',width=150)
        # fill=Both - fill both horizontally and expand =1 , it deals with the expansion of parent widget.
        self.student_table.pack(fill=BOTH,expand=1)
        # with the help of bind function will call the event    
        self.student_table.bind("<ButtonRelease>",self.get_data)
        self.fetch_data()
        
    
         
 
   #  --------------------------------------------------------PDF IS UNDER PROCESS----------------------------------------------------------------   




   
    def gen_pdf(self):
        try:
          pdf=SimpleDocTemplate("MyDoc.pdf")
          flow_obj=[]
          #table header
          td=[["ROLLNO","NAME","EMAIL","GENDER","CONTACT","DATEOFBIRTH","ADDRESS"]]
          con=pymysql.connect(host="localhost",user="root",password="",database="stm")
      #   cursor(): its a function with the help of this we can fires the queries.
          cur=con.cursor()
          cur.execute("select * from students")
          data_row=cur.fetchall()
          con.commit()
          con.close()
      #   print(data_row)
        
        
        except:    
          for row in data_row:
             data=[row[0],row[1],row[2],row[3],row[4],row[5],row[6]]
             td.append(data)
            # print(td)   
          table=Table(td) 
          ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.red),
                       ("BACKGROUND",(0,0),(-1,0),colors.yellow),
                       ("BACKGROUND",(0,1),(-1,-1),colors.lightskyblue)])                     
          table.setStyle(ts)
          flow_obj.append(table)
          pdf.build(flow_obj)
        else:
          messagebox.showinfo("Student Management System","Exported Into PDF successfully")



           

   
            
          
       
    

   #   WRITING CSV FILES WITH CSV
    def Export(self):
       con=pymysql.connect(host="localhost",user="root",password="",database="stm")
         # cursor(): its a function with the help of this we can fires the queries.
       cur=con.cursor()
       cur.execute("select * from students") 
       # Using with statement used in exception hanadling to make the code cleaner & much more readable
        
       with open("students.csv","w") as csv_file:
          # delimiter specifies the character used to separate each field.
          csv_writer=csv.writer(csv_file,delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)

            #WRITEROW () TAKES AN ITERABLE OF CELLS TO WRITE
          csv_writer.writerow([i[0] for i in cur.description])
            #WRITEROWS()  TAKES AN ITERABLE OF ITERABLES OF CELLS TO WRITE
          csv_writer.writerows(cur)
          #IMPORTED OS: getcwd() in Python returns the current working directory of a process.
       dir_path =os.getcwd() + "/students.csv"
       messagebox.showinfo("STUDENT MANAGEMENT SYSTEM","Exported INTO CSV successfully")





    def iExit(self):
       iExit=messagebox.askyesno("Student Database Management System","Confirm if you want to exit")
       if iExit > 0:
          root.destroy()
          import login 
          return 
   

   
        
          
      # re.compile() : used here it compiles a regex into a regex object.
      # Used boolean values here in return 
    
    
    def num_match(self,strg, search=re.compile(r'^[7-9]\d{9}$').search):

        return  bool(search(strg))
    
   
    
    def special_match(self,strg, search=re.compile(r'[^a-zA-Z.]').search):

        return not bool(search(strg))
    
    # this add() function calls in the add button      
    
    def add_student(self):
       # get():Gets the current contents of the entry field.
       if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="" or self.txt_address.get('1.0', 'end-1c')=="":
          messagebox.showerror("Error","All Fields Are Required !!!")
       

       elif self.special_match(self.name_var.get())==False:
            messagebox.showinfo("Error!", " Name should only have Characters")   
     
       elif self.num_match(self.contact_var.get())==False:
            messagebox.showinfo("Error!", "invalid Contact")

       elif  validate_email(self.email_var.get())==False:                
          messagebox.showinfo("student management system", "Please enter valid email(e.g.example@example.com)",icon='warning')  
       
       else:   
         # Creating database stm
         con=pymysql.connect(host="localhost",user="root",password="",database="stm")
         # cursor(): its a function with the help of this we can fires the queries.
         cur=con.cursor()
       
         cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(), 
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        # END:corresponds to the position just after the last character in the entry widget. 
                                                                        self.txt_address.get('1.0',END) # 1.0 defines the line number and END so get everything from first to end
                  
                                                                        ))
        
         # commit is the updating of a record in a database and ends a transaction within a relational database
         con.commit()
         self.fetch_data()
         self.clear()
         # close() function closes a previously opened database
         con.close()
         messagebox.showinfo("Success","Record has been inserted")
 
 
    
    def fetch_data(self):
       con=pymysql.connect(host="localhost",user="root",password="",database="stm")
       cur=con.cursor()
       cur.execute("select * from students")
       # cursor.fetchall() fetches all the rows of a query result. It returns all the rows as a list of tuples.
       rows=cur.fetchall()
       # if the length of rows is not equal to 0 then there should be some data
       if len(rows)!=0:
          # with this lines whatever the data will be there in that table will be deleted , means it will delete the children elements 
          self.student_table.delete(*self.student_table.get_children())
          for row in rows:
             self.student_table.insert('',END,values=row) # in values we passes the row.
          con.commit()
       con.close()     


    # used clear function because after inserting the data the entry fields should be clear enough.
   
    def clear(self):
       # set= set into blank it will delete the varaibles
       self.Roll_No_var.set("")
       self.name_var.set("")
       self.email_var.set("")
       self.gender_var.set("")
       self.contact_var.set("")
       self.dob_var.set("")
       # using delete function it will delete all the data from first line to the end
       self.txt_address.delete("1.0",END)

   
   
    def get_data(self,ev):
       # focus: its a function,set the focus item to item, otherwise returns the current focus item  
       data_row=self.student_table.focus()
       #item(): wherever our cursor will go in any row will come into this item(() function
       contents=self.student_table.item(data_row)
       # with the help of contents it will fetch all the values.
       row=contents['values']
        #print(row) 
       self.Roll_No_var.set(row[0])
       self.name_var.set(row[1])
       self.email_var.set(row[2])
       self.gender_var.set(row[3])
       self.contact_var.set(row[4])
       self.dob_var.set(row[5])
       # in address first we delete the data 
       self.txt_address.delete("1.0",END)
       # and then insert the data ,insert means in end our row help of index it will insert the data   
       self.txt_address.insert(END,row[6])

   
    
    def update_data(self):
       con=pymysql.connect(host="localhost",user="root",password="",database="stm")
       cur=con.cursor()
       
       cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                        
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_address.get('1.0',END),
                                                                        self.Roll_No_var.get()
                                                                        ))
       con.commit()
       self.fetch_data()
       self.clear()
       con.close()

    
    def Delete_data(self):
       messagebox.askquestion("Delete","Are You Sure?", icon='warning')
       if 'yes':   
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    
    
    def search_data(self):
       if self.search_txt.get()=="":
          messagebox.showerror("Error","Search Cannot be Empty")
  
       else:

           con=pymysql.connect(host="localhost",user="root",password="",database="stm")
           cur=con.cursor()
           #  LIKE operator is used in a WHERE clause to search for a specified pattern in a column.
           cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
           rows=cur.fetchall()
           if len(rows)!=0:
               self.student_table.delete(*self.student_table.get_children())

           elif len(rows)==0:
              messagebox.showerror("Error","No Record Found")

           for row in rows:
                  self.student_table.insert('',END,values=row)
                  con.commit()
           con.close()     




# object created
root=Tk()
ob=Student(root) # passed root inside in this
root.mainloop()  # mainloop() is an infinite loop used to run the application