import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont

class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1000x500+500+300")
        self.root.config(bg="#f2f2f2")

        # Set up a font
        self.heading_font = tkfont.Font(family='Helvetica', size=20, weight='bold')
        self.label_font = tkfont.Font(family='Helvetica', size=15,weight="bold")

        lbl_title=Label(self.root,text="REPORT",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1000,height=50)

        # Database connection
        self.conn = self.connect_to_db()
        self.cursor = self.conn.cursor()

        # Create heading label
        heading = Label(self.root,text="Hotel Management System",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        heading.pack(pady=50)

        # Create frame for combo box and buttons
        self.create_frame()

        # Create treeview to display data
        self.create_treeview()

    def connect_to_db(self):
        # Function to connect to MySQL
        return mysql.connector.connect(
            host="localhost",      
            user="root",          
            password="talent",   
            database="management"   
        )

    def create_frame(self):
        frame = Frame(self.root, bg="#f2f2f2")
        frame.pack(pady=10)

        # Combo box for Customer and Room
        combo_label = Label(frame, text="Choose Table:", font=self.label_font, bg="Black", fg="Gold")
        combo_label.grid(row=0, column=0, padx=10)

        self.combo = ttk.Combobox(frame, values=["Customer", "Room"], state="readonly")
        self.combo.grid(row=0, column=1, padx=10, pady=10)
        self.combo.current(0)

        # Create buttons for Show Table and Print Bill
        show_button = Button(frame, text="Show Table", command=self.show_table, bg="Black", fg="Gold", font=self.label_font, padx=10)
        show_button.grid(row=0, column=2, padx=10)

        print_button = Button(frame, text="Print Bill", command=self.print_bill, bg="Black", fg="Gold", font=self.label_font, padx=10)
        print_button.grid(row=0, column=3, padx=10)

    def create_treeview(self):
        # Create a Treeview to display tables
        tree_frame = Frame(self.root, bg="#f2f2f2")
        tree_frame.pack(pady=20)

        self.tree = ttk.Treeview(tree_frame, columns=('ID', 'Name', 'Details'), show='headings', height=10)
        self.tree.column("ID", width=100, anchor=CENTER)
        self.tree.column("Name", width=200, anchor=CENTER)
        self.tree.column("Details", width=200, anchor=CENTER)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Details', text='Details')
        self.tree.pack()

    def show_table(self):
        selection = self.combo.get()

        # Clear previous rows and reset column headings
        self.clear_tree()

        if selection == "Customer":
            # Query for customer table
            self.cursor.execute("SELECT Ref, Name, Mobile FROM customer")
            records = self.cursor.fetchall()

            # Configure Treeview columns for Customer table
            self.tree["columns"] = ('Ref', 'Name', 'Mobile')
            self.tree.heading('Ref', text='Ref')
            self.tree.heading('Name', text='Name')
            self.tree.heading('Mobile', text='Mobile')

            # Insert new rows
            for record in records:
                self.tree.insert("", END, values=record)

        elif selection == "Room":
            # Query for room table
            self.cursor.execute("SELECT roomavailable, roomtype, noOfdays FROM room")
            records = self.cursor.fetchall()

            # Configure Treeview columns for Room table
            self.tree["columns"] = ('roomavailable', 'roomtype', 'noOfdays')
            self.tree.heading('roomavailable', text='Room Available')
            self.tree.heading('roomtype', text='Room Type')
            self.tree.heading('noOfdays', text='No. of Days')

            # Insert new rows
            for record in records:
                self.tree.insert("", END, values=record)

    def clear_tree(self):
        # Clear the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

    def display_invoice(self, name, mobile, ref, no_of_days, room_no, amount, meal_package, meal_cost_per_day):
    # Generate invoice window
     invoice_window = Toplevel(self.root)
     invoice_window.title("Invoice")
     invoice_window.geometry("400x450")

    # Calculate total meal cost
     total_meal_cost = meal_cost_per_day * int(no_of_days)

    # Invoice details
     invoice_text = f"""
    ============================
    INVOICE
    ============================

     Customer Name: {name}
    Mobile: {mobile}
    Reference No: {ref}
    Room No: {room_no}
    No. of Days: {no_of_days}

    Room Cost Per Day: $3000.00
    Room Amount: ${amount - total_meal_cost:.2f}

    Meal Package: {meal_package}
    Meal Cost Per Day: ${meal_cost_per_day:.2f}
    Total Meal Amount: ${total_meal_cost:.2f}

    ----------------------------
    Total Amount: ${amount:.2f}
    ============================
    Thank you for your stay!
    """

     invoice_label = Label(invoice_window, text=invoice_text, justify=LEFT, font=("Helvetica", 12), bg="white")
     invoice_label.pack(pady=20)

     invoice_label = Label(invoice_window, text=invoice_text, justify=LEFT, font=("Helvetica", 12), bg="white")
     invoice_label.pack(pady=20)
    def print_bill(self):
       selected_item = self.tree.selection()
       if not selected_item:
        messagebox.showwarning("No Selection", "Please select a customer.")
        return

       item = self.tree.item(selected_item)
       if self.combo.get() == "Customer":
        customer_id, name, mobile = item['values']
        
        # Retrieve the room, noOfdays, and meal package using the contact (mobile) from room table
        self.cursor.execute("SELECT roomavailable, noOfdays, meal FROM room WHERE Contact = %s", (mobile,))
        result = self.cursor.fetchone()
        if result:
            room_no, no_of_days, meal_package = result

            # Room cost per day
            room_cost_per_day = 3000.0  # Updated room cost per day

            # Meal costs per day
            meal_costs = {
                "breakfast": 300.0,
                "lunch": 500.0,
                "dinner": 800.0
            }
            
            meal_total = 0

            # Calculate meal cost based on package type
            if meal_package == "Full":
                meal_total = meal_costs['breakfast'] + meal_costs['lunch'] + meal_costs['dinner']
            elif meal_package == "Half":
                meal_total = meal_costs['breakfast'] + meal_costs['lunch']
            elif meal_package == "Breakfast Only":
                meal_total = meal_costs['breakfast']
            else:
                meal_total = 300  # No meals

            # Calculate total costs
            room_amount = int(no_of_days) * room_cost_per_day
            total_meal_amount = int(no_of_days) * meal_total
            total_amount = room_amount + total_meal_amount

            # Display the invoice with room and meal details
            self.display_invoice(name, mobile, customer_id, no_of_days, room_no, total_amount, meal_package, meal_total)
        else:
            messagebox.showwarning("No Room Data", "No room information found for this customer.",parent=self.root)
       else:
        messagebox.showwarning("Invalid Selection", "Please select a customer to print the bill.",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    app = HotelManagement(root)
    root.mainloop()
