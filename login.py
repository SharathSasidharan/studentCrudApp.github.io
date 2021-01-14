from tkinter import*

from tkinter import messagebox
from validate_email import validate_email
import pymysql #pip install pymysql
import time

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
     
   
      


        # title=Label(self.root,text="Webcode Analog Clock",font=("times new roman",50,'bold'),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)
  #-------BACKGROUND COLORS: LEFT SIDE-----------------------------------------------     
        left_panel=Label(self.root,bg="#08A3D2",bd=0)
        left_panel.place(x=0,y=0,relheight=1,width=600)
  #------------------------------------------------------
  #--------BACKGROUND COLORS: RIGHT SIDE---------------------------------------------------
        right_panel=Label(self.root,bg="#031F3C",bd=0)
        right_panel.place(x=600,y=0,relheight=1,relwidth=1)
  #--------------------------------------------------------------
        #---------------------FRAMES------------------------------------------
         
        
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)
        #--------------------------------------------------------

        title=Label(login_frame,text="Login Here",font=("times new roman",30,'bold'),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="E-MAIL ADDRESS",font=("times new roman",18,'bold'),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35) 
        
        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,'bold'),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray",show='*')
        self.txt_pass_.place(x=250,y=280,width=350,height=35) 
        

        btn_reg=Button(login_frame,cursor="hand2",command=self.register_Window,text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)
       
        btn_login=Button(login_frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#031F3C",cursor="hand2",command=self.login_data).place(x=250,y=380,width=180,height=40)

    
       
    # if user not found it will redirect to register page 
    def register_Window(self):
          self.root.destroy()
          import register
          

    def clear(self):        
        self.txt_email.delete(0,END)
        self.txt_pass_.delete(0,END)      
        #--------------------------------------------------------------------------------------------
    def login_data(self):          


            if self.txt_email.get()=="" or  self.txt_pass_.get()=="":
             messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        
            elif validate_email(self.txt_email.get())==False:                
                    messagebox.showinfo("student management system", "Please enter valid email(e.g.example@example.com)",icon='warning')      
            
            elif len(self.txt_pass_.get())<8:
                 messagebox.showinfo("Error!", "Password Must be atleast 8 characters long")
        
            else:
                  try:
                        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                        cur=con.cursor()
                        cur.execute("select * from emp where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                        row=cur.fetchone()
                        # print(row)
                        if row==None:
                               messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root) 
                                     
                        else:
                               messagebox.showinfo("Success","Welcome",parent=self.root)
                               self.clear() 
                               self.root.destroy()
                               import student
                        con.close() 
                            


                  except Exception as e:
                        messagebox.showerror("Error",f"Error Due To:{str(e)}",parent=self.root)



        
    
root=Tk()
obj=Login(root)    # passed root inside in this
root.mainloop()    # mainloop() is an infinite loop used to run the application


