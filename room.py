from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from tkinter import Tk, Scrollbar, Frame
from tkcalendar import DateEntry
from datetime import datetime 
class Roombooking:
    def __init__(self,root) :
        self.root=root
        self.root.title("Hotel Management System ")
        self.root.geometry("1295x550+230+220")


    
       # current_date = datetime.now().date()

    # Get the selected dates
        #checkin_date = datetime.strptime(checkin_entry.get(), '%m/%d/%y').date()
        #checkout_date = datetime.strptime(txtcheck_out_date.get(), '%m/%d/%y').date()

    # Check if the check-in date is before the current date
       # if checkin_date < current_date:
       #   messagebox.showerror("Invalid Date", "Check-in date cannot be earlier than today!")
        #return

    # Check if the check-out date is before the check-in date
       # if checkout_date < checkin_date:
       #  messagebox.showerror("Invalid Date", "Check-out date must be later than the check-in date!")
       # return

    # If validation passes, print the dates (or further processing)
       # print(f"Check-in Date: {checkin_date}")
       # print(f"Check-out Date: {txtcheck_out_date}")
       # messagebox.showinfo("Booking Confirmation", f"Room booked from {checkin_date} to {checkout_date}")

        #===================================variables============================================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavaliable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        self.var_Bill=StringVar()
        self.checkin_entry=StringVar()
        self.checkout_entry=StringVar()

    







#====================================title====================================================================================

        lbl_title=Label(self.root,text="ROOM BOOKING Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #=================================LOGO=============================================================
        img2=Image.open(r"C:\Users\Pratham Sonigara\Desktop\itvedant\Project\Hotel Management System\Hotel Managment System\images\logohotel.png")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        #==========================LABEL FRAME=========================================
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new room ",12,"bold"),padx=2,)
        LabelFrameleft.place(x=5,y=50,width=425,height=490)
         #==================labels and entry====================================
# customer contact
        lbl_cust_contact=Label(LabelFrameleft,text="Customer Contact",font=("arial ",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W) 

        enty_contact=ttk.Entry(LabelFrameleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)
# Fetch data button
        btnFetchData=Button(LabelFrameleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="gold",width=9)
        btnFetchData.place(x=335,y=4)



        # Check_in Date
        Check_in_date=Label(LabelFrameleft,text="Check_in Date",font=("arial ",12,"bold"),padx=2,pady=6)
        Check_in_date.grid(row=1,column=0,sticky=W) 
        

        checkin_entry = DateEntry(LabelFrameleft,textvariable=self.checkin_entry,date_pattern="dd-mm-yyyy",width=25,font=("arial ",12,"bold"), background='Black', foreground='Gold', borderwidth=2,state="readonly")
        checkin_entry.grid(row=1, column=1)
       # print(self.checkin_entry)
       # txtcheck_in_date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
       # txtcheck_in_date.grid(row=1,column=1)
        # check_out Date
        Check_out_date=Label(LabelFrameleft,text="Check_out Date",font=("arial ",12,"bold"),padx=2,pady=6)
        Check_out_date.grid(row=2,column=0,sticky=W) 
       # print(checkout_entry)
        checkout_entry =DateEntry(LabelFrameleft,textvariable=self.checkout_entry,date_pattern="dd-mm-yyyy",font=("arial ",12,"bold"),width=25, background='Black', foreground='Gold', borderwidth=2,state="readonly")
        checkout_entry.grid(row=2, column=1,)
        print(checkout_entry)
       # txtcheck_out_date=ttk.Entry(LabelFrameleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
       # txtcheck_out_date.grid(row=2,column=1)
        #Roomtype
        Label_roomtype=Label(LabelFrameleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        Label_roomtype.grid(row=3,column=0,sticky=W) 

        conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()
        combo_Roomtype=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Roomtype["value"]=ide
        combo_Roomtype.current(0)
        combo_Roomtype.grid(row=3,column=1)
         # Available Rooms
        lblRoomAvailable=Label(LabelFrameleft,text="Rooms Available ",font=("arial ",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W) 

        conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomavaliable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)
        # Meal
        lblMeal=Label(LabelFrameleft,text="Meal",font=("arial ",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W) 

        txtMeal=ttk.Entry(LabelFrameleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)
        # no of days
        lblNoofdays=Label(LabelFrameleft,text="No of Days",font=("arial ",12,"bold"),padx=2,pady=6)
        lblNoofdays.grid(row=6,column=0,sticky=W) 

        txtNoofdays=ttk.Entry(LabelFrameleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txtNoofdays.grid(row=6,column=1)
        # Paid Tax
        lblNoofdays=Label(LabelFrameleft,text="Paid Tax",font=("arial ",12,"bold"),padx=2,pady=6)
        lblNoofdays.grid(row=7,column=0,sticky=W) 

        txtNoofdays=ttk.Entry(LabelFrameleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txtNoofdays.grid(row=7,column=1)
        # Sub Total
        lblNoofdays=Label(LabelFrameleft,text=" Sub Total ",font=("arial ",12,"bold"),padx=2,pady=6)
        lblNoofdays.grid(row=8,column=0,sticky=W) 

        txtNoofdays=ttk.Entry(LabelFrameleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        txtNoofdays.grid(row=8,column=1)
        # Total Cost
        lblIdNumber=Label(LabelFrameleft,text=" Total Cost ",font=("arial ",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W) 

        txtIdNumber=ttk.Entry(LabelFrameleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)
        #=====================bill button=================
        btnBill=Button(LabelFrameleft,text="Bill",command=self.calculate_bill,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

         #===============================btns================================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
   

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.clear_inputs,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #========================Right side image=======================================
        img3=Image.open(r"C:\Users\Pratham Sonigara\Desktop\itvedant\Project\Hotel Management System\Hotel Managment System\images\bed.jpg")
        img3=img3.resize((520,250))
        self.photoimg3=ImageTk.PhotoImage(img3)


        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=250)



        #==================================table frame search system=======================================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2,)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2) 

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact")
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
        details_table.place(x=0,y=50,width=860,height=180)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomsavailable","meal","noofdays"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room-Type")
        self.room_table.heading("roomsavailable",text="Room no")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="NoofDays")
        
        self.room_table["show"]="headings"
        self.room_table.column("contact",width=120)
        self.room_table.column("checkin",width=120)
        self.room_table.column("checkout",width=120)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomsavailable",width=100)
        self.room_table.column("meal",width=120)        
        self.room_table.column("noofdays",width=120)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
   # #def convert_date_format(self):
    # try:
        # Get the current date
     #     current_date = datetime.now().date()

        # Get the check-in and check-out dates
     #     checkin_date = self.checkin_entry.get()
      #    checkout_date = self.checkout_entry.get()

        # Convert the dates to datetime objects
      #    checkin_date_obj = datetime.strptime(checkin_date, '%Y-%m-%d').date()
      #    checkout_date_obj = datetime.strptime(checkout_date, '%Y-%m-%d').date()

        # Validate the dates
      #    if checkin_date_obj > current_date:
      #      messagebox.showerror("Invalid Date", "Check-in date cannot be later than today!")
      #      return
      #    if checkout_date_obj > current_date:
      #      messagebox.showerror("Invalid Date", "Check-out date cannot be later than today!")
      #      return
      #    if checkout_date_obj < checkin_date_obj:
      #      messagebox.showerror("Invalid Date", "Check-out date must be later than the check-in date!")
      #      return

        # Convert the dates to the desired format (e.g., dd-mm-yyyy)
      #    formatted_checkin_date = checkin_date_obj.strftime('%d-%m-%Y')
       #   formatted_checkout_date = checkout_date_obj.strftime('%d-%m-%Y')

        # Update the variables with the formatted dates
       #   self.var_checkin.set(formatted_checkin_date)
       #   self.var_checkout.set(formatted_checkout_date)

    # except ValueError:
     #   messagebox.showerror("Invalid Format", "Please enter a valid date or format.")




        #add data
    def add_data(self):
    # Check if any required field is empty
      if self.checkout_entry.get() == "" or self.checkin_entry.get() == "" or self.var_contact.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
        return  # Exit function if validation fails

      else:
        try:
            # Establish database connection
            conn = mysql.connector.connect(host="localhost", username="root", password="talent", database="management")
            my_cursor = conn.cursor()

            # Execute the insert query
            my_cursor.execute("INSERT INTO room VALUES(%s,%s,%s,%s,%s,%s,%s)", (
                self.var_contact.get(),
                self.checkin_entry.get(),
                self.checkout_entry.get(),
                self.var_roomtype.get(),
                self.var_roomavaliable.get(),
                self.var_meal.get(),
                self.var_noofdays.get()
            ))

            conn.commit()  # Save changes to the database
            self.fetch_data()  # Refresh the data in the table after inserting
            conn.close()  # Close the database connection

            # Show success message
            messagebox.showinfo("Success", "Room Booked", parent=self.root)

        except Exception as es:
            # Show warning message in case of any exception
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select* from room")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
          self.room_table.delete(*self.room_table.get_children())
          for i in rows:
              self.room_table.insert("",END,values=i)
         conn.commit()
         conn.close()

         # get cuersor
    def get_cuersor(self,events=""):
        cusrsor_row=self.room_table.focus()
        content=self.room_table.item(cusrsor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavaliable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

        #update function
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter mobile number",parent=self.root)
        else:  
          conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("update room set Contact=%s,Check_in=%s,Check_out=%s,roomtype=%s,meal=%s,noOfdays=%s,Bill=%s  where Contact=%s",(
                                                                                                                                                                     
                                                                                                                                    self.var_checkin.get(),
                                                                                                                                    self.var_checkout.get(),
                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                    self.var_roomavaliable.get(),
                                                                                                                                    self.var_meal.get(),
                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                    self.var_Bill.get(),
                                                                                                                                    self.var_contact.get()
                                                                                                                                      ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Update","Room Details have been Updated Successfully",parent=self.root)   
    # Delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room ",parent= self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset function
    def clear_inputs(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavaliable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
      #  self.checkin_entry.set("")
      #  self.checkout_entry.set("")













#all data fetch

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()


            if row==None:
                messagebox.showerror("Error","This Number not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
#==============================Data frame========================================
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)
#Name
                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
               #Gender
                conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #Email
                conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #Address
                conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)
    #def convert_date_format(self):
    #  try:
    #    # Get the current date
    #    current_date = datetime.now().date()

    #    # Get the check-in and check-out dates
    #    checkin_date = self.checkin_entry.get()
    #    checkout_date = self.checkout_entry.get()

    #    # Convert the dates to datetime objects
    #    checkin_date_obj = datetime.strptime(checkin_date, '%d-%m-%Y').date()
    #    checkout_date_obj = datetime.strptime(checkout_date, '%d-%m-%Y').date()

        # Validate the dates
    #    if checkin_date_obj > current_date:
     #       messagebox.showerror("Invalid Date", "Check-in date cannot be later than today!")
     ##       return
     ##   if checkout_date_obj > current_date:
     ###       messagebox.showerror("Invalid Date", "Check-out date cannot be later than today!")
      ###      return
     ## #  if checkout_date_obj < checkin_date_obj:
     ####       messagebox.showerror("Invalid Date", "Check-out date must be later than the check-in date!")
     ###       return#
#
     ## #  # Convert the dates to the desired format (e.g., dd-mm-yyyy)
#     ###   formatted_checkin_date = checkin_date_obj.strftime('%d-%m-%Y')
 #    ##   formatted_checkout_date = checkout_date_obj.strftime('%d-%m-%Y')#
#
      # # # Update the variables with the formatted dates
#     # #  self.var_checkin.set(formatted_checkin_date)
 #     #  self.var_checkout.set(formatted_checkout_date)

      #except:
       # pass

# search system
    def search(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="talent",database="management")
          my_cursor=conn.cursor()
          #my_cursor.execute("select*from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
          search_value = self.txt_search.get()
          
          query = "SELECT * FROM room WHERE contact LIKE  %s"
          params = (f"%{search_value}%",)
          my_cursor.execute(query, params)
          row=my_cursor.fetchall()
          if len (row)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in row:
                  self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()



    def calculate_bill(self):
        # Room cost per day for Luxury Room
        room_cost_per_day = 3000.0
        
        # Meal costs per day
        meal_costs = {
            "breakfast": 300.0,
            "lunch": 500.0,
            "dinner": 800.0
        }
        
        try:

            checkin_date=self.checkin_entry.get()
            checkout_date=self.checkout_entry.get()

            checkin_date = datetime.strptime(self.checkin_entry.get(), '%d-%m-%Y').date()
            checkout_date = datetime.strptime(self.checkout_entry.get(), '%d-%m-%Y').date()

# Convert to string in yyyy-mm-dd format before saving
            checkin_str = checkin_date.strftime('%Y-%m-%d')
            checkout_str = checkout_date.strftime('%Y-%m-%d')
            # Get the check-in and check-out dates
            #checkin_date = datetime.strptime(self.checkin_entry.get(), '%d-%m-%Y').date()
            #checkout_date = datetime.strptime(self.checkout_entry.get(), '%d-%m-%Y').date()

          #  date_pattern="dd-mm-yyyy"
            
           # datetime.now()
# Convert string dates to datetime objects
            #checkin_date_obj = datetime.strptime(checkin_date,date_pattern)
           # checkout_date_obj = datetime.strptime(checkout_date,date_pattern)

# Calculate the number of days
            no_of_days = (checkout_date - checkin_date).days

            if no_of_days < 1:
                 raise ValueError("Check-out date must be after check-in date.")

            
            # Get the meal type and calculate the meal cost
            meal_type = self.var_meal.get().strip().lower()
            if meal_type not in meal_costs:
                raise ValueError("Invalid meal type. Choose Breakfast, Lunch, or Dinner.")
            
            meal_cost = no_of_days * meal_costs[meal_type]
            
            # Calculate the room cost
            room_cost = no_of_days * room_cost_per_day
            
            # Sub total (Room cost + Meal cost)
            sub_total = room_cost + meal_cost
            
            # Tax calculation (e.g., 9% tax)
            tax = sub_total * 0.00
            
            # Total cost after tax
            total_cost = sub_total + tax
            
            # Set the calculated values to the respective variables
            self.var_noofdays.set(no_of_days)
            self.var_paidtax.set(f"Rs. {tax:.2f}")
            self.var_actualtotal.set(f"Rs. {sub_total:.2f}")
            self.var_total.set(f"Rs. {total_cost:.2f}")
        
        except ValueError as e:
            # Display an error message if the input is invalid
            messagebox.showerror("Input Error", str(e))


   

       














        

        












if __name__=="__main__":
   roottk=Tk()
   obj=Roombooking(roottk)
   roottk.mainloop()
    

