import tkinter as tk
from tkinter import messagebox
import mysql.connector

class MedicineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medicine Supply Management")

        # Database connection
        self.conn = None
        self.cursor = None

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Form for CRUD operations
        tk.Label(self.root, text="ID:").grid(row=0, column=0, padx=10, pady=5)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(self.root, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Expiry Date (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
        self.expiry_entry = tk.Entry(self.root)
        self.expiry_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Connect", command=self.connect_to_database).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(self.root, text="Add", command=self.add_medicine).grid(row=6, column=0, pady=5)
        tk.Button(self.root, text="Update", command=self.update_medicine).grid(row=6, column=1, pady=5)
        tk.Button(self.root, text="Delete", command=self.delete_medicine).grid(row=7, column=0, pady=5)
        tk.Button(self.root, text="View All", command=self.view_all_medicines).grid(row=7, column=1, pady=5)

        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def connect_to_database(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2002",
                database="medicine_supply"
            )
            self.cursor = self.conn.cursor()
            messagebox.showinfo("Connection Status", "Connected successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def add_medicine(self):
        try:
            sql = "INSERT INTO medicines (name, quantity,expiry_date) VALUES (%s, %s, %s)"
            values = (self.name_entry.get(), int(self.quantity_entry.get()), self.expiry_entry.get())
            self.cursor.execute(sql, values)
            self.conn.commit()
            messagebox.showinfo("Success", "Medicine added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def update_medicine(self):
        try:
            sql = "UPDATE medicines SET name = %s, quantity = %s, expiry_date = %s WHERE id = %s"
            values = (self.name_entry.get(), int(self.quantity_entry.get()),self.expiry_entry.get(), int(self.id_entry.get()))
            self.cursor.execute(sql, values)
            self.conn.commit()
            messagebox.showinfo("Success", "Medicine updated successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def delete_medicine(self):
        try:
            sql = "DELETE FROM medicines WHERE id = %s"
            self.cursor.execute(sql, (int(self.id_entry.get()),))
            self.conn.commit()
            messagebox.showinfo("Success", "Medicine deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def view_all_medicines(self):
        try:
            self.cursor.execute("SELECT * FROM medicines")
            rows = self.cursor.fetchall()
            self.result_text.delete(1.0, tk.END)
            for row in rows:
                self.result_text.insert(tk.END, str(row) + "\n")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicineApp(root)
    root.mainloop()
