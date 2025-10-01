from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from tkinter import Tk, Scrollbar, Frame
class Cust_Win:
    def __init__(self,root) :
        self.root=root
        self.root.title("Hotel Management System ")
        self.root.geometry("1295x550+230+220")

        #==========================variable======================================
        self.var_ref=StringVar( )
        X=random.randint(1000,9999)
        self.var_ref.set(str(X))


        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
  #===========================title=============================================================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #=================================LOGO=============================================================
        img2=Image.open(r"C:\Users\Pratham Sonigara\Desktop\itvedant\Project\Hotel Management System\Hotel Managment System\images\logohotel.png")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #=============================LABEL FRAME====================
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new room ",12,"bold"),padx=2,)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)

        #==================labels and entry====================================

        lbl_cust_ref=Label(LabelFrameleft,text="Customer Ref",font=("arial ",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W) 

        enty_ref=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_ref,font=("times new room ",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

        #===============cust name=========================
        cname=Label(LabelFrameleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W) 

        cname=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_cust_name,font=(" arial ",13,"bold"))
        cname.grid(row=1,column=1)
        #====================mother name===================================
        lblmname=Label(LabelFrameleft,font=("arial",12,"bold"),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W) 

        lblmname=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_mother,font=(" arial ",13,"bold"))
        lblmname.grid(row=2,column=1)

        #=================gender combobox=================================
        Label_gender=Label(LabelFrameleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        Label_gender.grid(row=3,column=0,sticky=W) 
        combo_gender=ttk.Combobox(LabelFrameleft,font=("arial",12,"bold"),textvariable=self.var_gender,width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        #===================postcode=======================================
        lblPostcode=Label(LabelFrameleft,font=("arial",12,"bold"),text="Postcode:",padx=2,pady=6)
        lblPostcode.grid(row=4,column=0,sticky=W) 

        lblPostcode=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_post,font=(" arial ",13,"bold"))
        lblPostcode.grid(row=4,column=1)

        #=========================mobile number =================================
        lblMobile=Label(LabelFrameleft,font=("arial",12,"bold"),text="Mobile Number:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W) 

        lblMobile=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_mobile,font=("arial",13,"bold"))
        lblMobile.grid(row=5,column=1)
        #=======================Email================================================
        lblEmail=Label(LabelFrameleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W) 

        lblEmail=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_email,font=(" arial ",13,"bold"))
        lblEmail.grid(row=6,column=1)
       #===============================nationality combobox===============================
        lblNationality=Label(LabelFrameleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        combo_Nationality=ttk.Combobox(LabelFrameleft,font=("arial",12,"bold"),textvariable=self.var_nationality,width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","Britist")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)
 #===============================idproof type combobox=======================================
        lblIdProof=Label(LabelFrameleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W) 
        combo_IdProof=ttk.Combobox(LabelFrameleft,font=("arial",12,"bold"),textvariable=self.var_id_proof,width=27,state="readonly")
        combo_IdProof["value"]=("AdharCard","Passport","Driving License")
        combo_IdProof.current(0)
        combo_IdProof.grid(row=8,column=1)
 #===============================id number=============================================
        lblIdNumber=Label(LabelFrameleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W) 

        lblIdNumber=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_id_number,font=(" arial ",13,"bold"))
        lblIdNumber.grid(row=9,column=1)
        #================================address====================================
        lblAddress=Label(LabelFrameleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W) 

        lblAddress=ttk.Entry(LabelFrameleft,width=29,textvariable=self.var_address,font=(" arial ",13,"bold"))
        lblAddress.grid(row=10,column=1)

        #===============================btns================================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
   

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #======================table frame==============================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2,)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2) 

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Reference.no")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,width=24,textvariable=self.txt_search,font=(" arial ",13,"bold"),)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show ALL",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #================================SHOW TABLE===========================================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill="x")
        Scroll_y.pack(side=RIGHT,fill="y")

        Scroll_x.config(command=self.Cust_Details_Table.xview)
        Scroll_y.config(command=self.Cust_Details_Table.yview)


        self.Cust_Details_Table.heading("ref",text="Refer no")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="mothername")
        self.Cust_Details_Table.heading("gender",text="gender")
        self.Cust_Details_Table.heading("post",text="postcode")
        self.Cust_Details_Table.heading("mobile",text="mobile no")
        self.Cust_Details_Table.heading("email",text="email")
        self.Cust_Details_Table.heading("nationality",text="nationality")
        self.Cust_Details_Table.heading("idproof",text="idproof")
        self.Cust_Details_Table.heading("idnumber",text="idnumber")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)        
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
    def add_data(self):
      if not self.var_cust_name.get().isalpha():
        messagebox.showerror("Invalid Input", "Customer Name must contain only letters.",parent=self.root)
      elif not self.var_mother.get().isalpha():
        messagebox.showerror("Invalid Input", "Mother's Name must contain only letters.",parent=self.root)
      elif not self.var_post.get().isdigit() or len(self.var_post.get()) > 6:
        messagebox.showerror("Invalid Input", "Postcode should not be more than 6 digits.",parent=self.root)
      elif not self.var_mobile.get().isdigit() or len(self.var_mobile.get()) > 10:
        messagebox.showerror("Invalid Input", "Mobile Number must not be more than 10 digits.",parent=self.root)
      elif not self.var_email.get().endswith("@gmail.com"):
         messagebox.showerror("Invalid Input", "Email must contain @gmail.com",parent=self.root)
      elif not self.var_address.get().replace(" ", "").isalpha():
        messagebox.showerror("Invalid Input", "Address must contain only letters.",parent=self.root)
      elif self.var_mobile.get() == "" or self.var_mother.get() == "":
        messagebox.showerror("Invalid Input", "All fields are required.",parent=self.root)
      else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="talent", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)", (
                self.var_ref.get(),
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Customer has been added", parent=self.root)
        except Exception as es:
            messagebox.showwarning("warning", f"Something went wrong: {str(es)}", parent=self.root)









   # def add_data(self):
   #     add_data=messagebox.showerror("Invalid Input", "Customer Name must contain only letters.")#
   #     if self.var_mobile.get()==" " or self.var_mother.get()== "":
   #          messagebox.showerror("Error","All fields are required",parent=self.root)
   #     else:
   #         try:
   #           conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
   #           my_cursor=conn.cursor()
   #           my_cursor.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
   #                                                                           self.var_ref.get(),
   #                                                                           self.var_cust_name.get(),
   #                                                                           self.var_mother.get(),
   #                                                                           self.var_gender.get(),
   #                                                                           self.var_post.get(),
   #                                                                           self.var_mobile.get(),
   #                                                                           self.var_email.get(),
   #                                                                           self.var_nationality.get(), 
   #                                                                           self.var_id_proof.get(),
   #                                                                           self.var_id_number.get(),
   #                                                                           self.var_address.get()
   #                                                                        ))
   #           conn.commit()
   #           self.fetch_data()
   #           conn.close()
   #           messagebox.showinfo("Success","Customer has been added",parent=self.root)
   #         except Exception as es:
   #           messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select* from customer")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
          self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
          for i in rows:
              self.Cust_Details_Table.insert("",END,values=i)
         conn.commit()
         conn.close()
    def get_cuersor(self,events=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
    def update(self):
        if not self.var_cust_name.get().isalpha():
           messagebox.showerror("Invalid Input", "Customer Name must contain only letters.",parent=self.root)
        elif not self.var_mother.get().isalpha():
          messagebox.showerror("Invalid Input", "Mother's Name must contain only letters.",parent=self.root)
        elif not self.var_post.get().isdigit() or len(self.var_post.get()) > 6:
         messagebox.showerror("Invalid Input", "Postcode should not be more than 6 digits.",parent=self.root)
        elif not self.var_mobile.get().isdigit() or len(self.var_mobile.get()) > 10:
         messagebox.showerror("Invalid Input", "Mobile Number must not be more than 10 digits.",parent=self.root)
        elif not self.var_email.get().endswith("@gmail.com"):
         messagebox.showerror("Invalid Input", "Email must contain @gmail.com",parent=self.root)
        elif not self.var_address.get().replace(" ", "").isalpha():
         messagebox.showerror("Invalid Input", "Address must contain only letters.",parent=self.root)
        elif self.var_mobile.get() == "" or self.var_mother.get() == "":
         messagebox.showerror("Invalid Input", "All fields are required.",parent=self.root)
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter mobile number",parent=self.root)
        else:  
          conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("update customer set Name=%s,mother=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where Ref=%s",(
                                                                                                                                                                     
                                                                                                                                                                     self.var_cust_name.get(),
                                                                                                                                                                     self.var_mother.get(),
                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                     self.var_post.get(),
                                                                                                                                                                     self.var_mobile.get(),
                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                     self.var_nationality.get(),
                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                     self.var_id_proof.get(),
                                                                                                                                                                     self.var_id_number.get(), 
                                                                                                                                                                     self.var_ref.get() 
                                                                                                                                                                                                  ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Update","Customer Details have been Updated Successfully",parent=self.root)
    def mDelete(self):
        if not self.var_cust_name.get().isalpha():
          messagebox.showerror("Invalid Input", "Customer Name must contain only letters.",parent=self.root)
        elif not self.var_mother.get().isalpha():
         messagebox.showerror("Invalid Input", "Mother's Name must contain only letters.",parent=self.root)
        elif not self.var_post.get().isdigit() or len(self.var_post.get()) > 6:
         messagebox.showerror("Invalid Input", "Postcode should not be more than 6 digits.",parent=self.root)
        elif not self.var_mobile.get().isdigit() or len(self.var_mobile.get()) > 10:
         messagebox.showerror("Invalid Input", "Mobile Number must not be more than 10 digits.",parent=self.root)
        elif not self.var_email.get().endswith("@gmail.com"):
         messagebox.showerror("Invalid Input", "Email must contain @gmail.com",parent=self.root)
        elif not self.var_address.get().replace(" ", "").isalpha():
         messagebox.showerror("Invalid Input", "Address must contain only letters.",parent=self.root)
        elif self.var_mobile.get() == "" or self.var_mother.get() == "":
         messagebox.showerror("Invalid Input", "All fields are required.")
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer ",parent= self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
    #self.var_ref.set(""),
       self.var_cust_name.set(""),
       self.var_mother.set(""),
      #self.var_gender.set(""),
       self.var_post.set(""),
       self.var_mobile.set(""),
       self.var_email.set(""),
    #self.var_nationality.set(""),
    #self.var_id_proof.set(""),
       self.var_id_number.set(""),
       self.var_address.set("")
       X=random.randint(1000,9999)
       self.var_ref.set(str(X))
    def search(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
          my_cursor=conn.cursor()
          #my_cursor.execute("select*from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
          search_value = self.txt_search.get()
          
          query = "SELECT * FROM customer WHERE Ref LIKE  %s"
          params = (f"%{search_value}%",)
          my_cursor.execute(query, params)
          row=my_cursor.fetchall()
          if len (row)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in row:
                  self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
            conn.close()

    #def validate_inputs(self):
    #    customer_name = self.var_cust_name.get()
    #    mother_name = self.var_mother.get()
    #    postcode = self.var_post.get()
    #    mobile_number = self.var_mobile.get()

        # Check if customer name and mother name are alphabetic
    #    if not customer_name.isalpha():
    #        messagebox.showerror("Invalid Input", "Customer Name must contain only letters.")
    #        return
    #    if not mother_name.isalpha():
    #        messagebox.showerror("Invalid Input", "Mother Name must contain only letters.")
    #        return

    #    # Check if postcode is a digit and not more than 6 digits
    #    if not postcode.isdigit() or len(postcode) > 6:
    #        messagebox.showerror("Invalid Input", "Postcode must be a number and not more than 6 digits.")
    #        return

        # Check if mobile number is a digit and not more than 10 digits
    #    if not mobile_number.isdigit() or len(mobile_number) > 10:
    #        messagebox.showerror("Invalid Input", "Mobile number must be a number and not more than 10 digits.")
    #        return

        # If everything is valid
    #    messagebox.showinfo("Success", "All inputs are valid!")



    
        

            

        


    pass 
if __name__=="__main__":
   roottk=Tk()
   obj=Cust_Win(roottk)
   roottk.mainloop()
    


