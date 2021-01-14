from tkinter import*               #imported tkinter file  
from tkinter import ttk            #It Provides Combo Boxes
from tkinter import messagebox     # MessageBox Widget is used to display the message boxes in the python applications
import re                          # re to work with RegEx
from PIL import Image,ImageTk      #PIP INSTALL PILLOW TO DEAL WITH JPG IMAGES 
import pymysql                     #PIP INSTAll PYMYSQL
from validate_email import validate_email  #Validate_email is a package for Python that check if an email is valid, properly formatted and really exists.
class Register:
     # we have to Initialize the constructor
    def __init__(self,root):
        #first need to initalize the root   
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')
      
         
         # BACKGROUND IMAGE
        self.bg=ImageTk.PhotoImage(file="images/back.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)


         # LEFT IMAGE
        self.left=ImageTk.PhotoImage(file="images/side.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

    
            # REGISTER FRAME
        frame1=Frame(self.root,bg='white')
        frame1.place(x=480,y=100,width=700,height=500)   
        title=Label(frame1,text="STUDENT REGISTRATION FORM ",font=("times new roman",20,'bold'),bg="white",fg="blue").place(x=50,y=30)
              
                 
        # converted All ENTRY objects into self
        fname=Label(frame1,text="First Name",font=("times new roman",15,'bold'),bg="white",fg="grey").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=250)
   
        lname=Label(frame1,text="Last Name",font=("times new roman",15,'bold'),bg="white",fg="grey").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_lname.place(x=370,y=130,width=250)
         #---------------------------

        contact=Label(frame1,text="Contact No",font=("times new roman",15,'bold'),bg="white",fg="grey").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,'bold'),bg="white",fg="grey").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_email.place(x=370,y=200,width=250)
         
          #---------------------------

        question=Label(frame1,text="Security Question",font=("times new roman",15,'bold'),bg="white",fg="grey").place(x=50,y=240)     

        self.combo_question=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.combo_question['values']=("Select","Your First Nickname","Your Favourite Color","Your Favourite Programming Language")
        self.combo_question.place(x=50,y=270,width=250)
        self.combo_question.current(0)   # this line gives the current value in comboboxes ie select  its in 0 index so it will show there in boxes
       
        answer=Label(frame1,text="Answer",font=("times new roman",15,'bold'),bg="white",fg="grey").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_answer.place(x=370,y=270,width=250)
        #-----------
        password=Label(frame1,text="Password",font=("times new roman",15,'bold'),bg="white",fg="grey").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgrey",show='*')
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,'bold'),bg="white",fg="grey").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgrey",show='*')
        self.txt_cpassword.place(x=370,y=340,width=250)
       
       
         # TERMS AND CONDITIONDS 
        # reason I used variable here because in onvalue and offvalue I have passed the INT value , means if the checkbox is check it returns 1 else returns 0
        self.chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",var=self.chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        # Image can be added with the help of PhotoImage() method     
        # file = "path_of_file"
        self.btn_img=ImageTk.PhotoImage(file="images/register1.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor='hand2',command=self.register_data).place(x=50,y=420)
         # cursors - mouse cursors available in Tk ,so want my cursor to change into a "hand" when my cursor is hovering over it.I also want to change my cursor back into an arrow when the cursor leaves the area occupied by the label.
        btn_login=Button(self.root,text="Sign In",command=self.login_Window,font=("times new roman",20),bg='white',bd=0,cursor='hand2').place(x=200,y=530,width=150)

    def num_match(self,strg, search=re.compile(r'^[7-9]\d{9}$').search):

        return  bool(search(strg))

    def special_match(self,strg, search=re.compile(r'[^a-zA-Z.]').search):

        return not bool(search(strg))  
          
    def login_Window(self):
        
          self.root.destroy()  
          import login
          
          
    # It Will clears the fields after it gets inserted
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_answer.delete(0,END)
        self.combo_question.current(0)

    def register_data(self):
        

         if self.txt_fname.get()=="" or  self.txt_contact.get()==""  or  self.txt_email.get()=="" or self.combo_question.get()=="Select"  or self.txt_answer.get()=="":
             # show a error message of parent window ie.self.root
             messagebox.showerror("Error","All Fields Are Required",parent=self.root)
         elif self.special_match(self.txt_fname.get() and self.txt_lname.get())==False:
            messagebox.showwarning("Error!", " Name should only have Characters", icon="warning")   

         elif self.special_match(self.txt_answer.get())==False:
            messagebox.showwarning("Error!", " Name should only have Characters", icon="warning")   
            
         elif self.num_match(self.txt_contact.get())==False:
            messagebox.showinfo("Error!", "Invalid Number ")

         elif validate_email(self.txt_email.get())==False:                
                    messagebox.showinfo("student management system", "Please enter valid email(e.g.example@example.com)",icon='warning')    
         # if the password is not equal to the confirm password show a messagebox
         elif self.txt_password.get()!=self.txt_cpassword.get():
              messagebox.showerror("Error","Password & Confirm password should be same ",parent=self.root)
         elif len(self.txt_password.get() and self.txt_cpassword.get())<8:
                 messagebox.showinfo("Error!", "Password Must be atleast 8 characters long")     
          # if its equal to 0 means its not checked then shows a error message
         
         elif self.chk.get()==0:
              messagebox.showerror("Error","Please Agree our Terms & Conditions",parent=self.root)

         else:
             try:
                 con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                 cur=con.cursor()
                 #This query will check the condition that user exist with same mail-id or not 
                 cur.execute("Select* from emp where email=%s",self.txt_email.get())
                 # fetchone(): This method returns one record as a tuple, If there are no more records then it returns None.
                 row=cur.fetchone()
                 # print(row)
                 #if user already exists with the same email-id it will show a message
                 if row!=None:
                     messagebox.showerror("Error","User already Exist With this Email-id ",parent=self.root)
                 else:     

                      cur.execute("insert into emp (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                             (self.txt_fname.get(),  
                              self.txt_lname.get(),
                              self.txt_contact.get(),
                              self.txt_email.get(),
                              self.combo_question.get(),
                              self.txt_answer.get(),
                              self.txt_password.get()   
                             ))
                 
                      con.commit()              
                      con.close()
                      messagebox.showinfo("Success","Register Successfull",parent=self.root)
                      # clear() function calls here after successfully data inserted 
                      self.clear()
             except Exception as e:
                  messagebox.showerror("Error",f"Error due to : {str(e)}",parent=self.root)


root=Tk()
obj=Register(root)     # passed root inside in this
root.mainloop()        # mainloop() is an infinite loop used to run the application
