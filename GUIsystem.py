import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pickle
import os


class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details


class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget


class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details


class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client, guest_list, suppliers):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client = client
        self.guest_list = guest_list
        self.suppliers = suppliers


class EmployeeManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")

        self.tabControl = ttk.Notebook(master)
        self.tabControl.pack(expand=1, fill="both")

        self.employee_tab = ttk.Frame(self.tabControl)
        self.client_tab = ttk.Frame(self.tabControl)
        self.supplier_tab = ttk.Frame(self.tabControl)
        self.event_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.employee_tab, text="Employees")
        self.tabControl.add(self.client_tab, text="Clients")
        self.tabControl.add(self.supplier_tab, text="Suppliers")
        self.tabControl.add(self.event_tab, text="Events")

        self.employee_table = ttk.Treeview(self.employee_tab,
                                           columns=('Name', 'ID', 'Department', 'Job Title', 'Salary'))
        self.employee_table.heading('Name', text='Name')
        self.employee_table.heading('ID', text='ID')
        self.employee_table.heading('Department', text='Department')
        self.employee_table.heading('Job Title', text='Job Title')
        self.employee_table.heading('Salary', text='Salary')
        self.employee_table.pack(expand=1, fill="both")

        self.load_employees()

        self.client_table = ttk.Treeview(self.client_tab,
                                         columns=('ID', 'Name', 'Address', 'Contact Details', 'Budget'))
        self.client_table.heading('ID', text='ID')
        self.client_table.heading('Name', text='Name')
        self.client_table.heading('Address', text='Address')
        self.client_table.heading('Contact Details', text='Contact Details')
        self.client_table.heading('Budget', text='Budget')
        self.client_table.pack(expand=1, fill="both")

        self.load_clients()

        self.supplier_table = ttk.Treeview(self.supplier_tab, columns=('ID', 'Name', 'Address', 'Contact Details'))
        self.supplier_table.heading('ID', text='ID')
        self.supplier_table.heading('Name', text='Name')
        self.supplier_table.heading('Address', text='Address')
        self.supplier_table.heading('Contact Details', text='Contact Details')
        self.supplier_table.pack(expand=1, fill="both")

        self.load_suppliers()

        self.event_table = ttk.Treeview(self.event_tab,
                                        columns=('ID', 'Type', 'Theme', 'Date', 'Time', 'Duration', 'Venue', 'Client'))
        self.event_table.heading('ID', text='ID')
        self.event_table.heading('Type', text='Type')
        self.event_table.heading('Theme', text='Theme')
        self.event_table.heading('Date', text='Date')
        self.event_table.heading('Time', text='Time')
        self.event_table.heading('Duration', text='Duration')
        self.event_table.heading('Venue', text='Venue')
        self.event_table.heading('Client', text='Client')
        self.event_table.pack(expand=1, fill="both")

        self.load_events()

        self.add_employee_button = tk.Button(self.employee_tab, text="Add Employee", command=self.add_employee_dialog)
        self.add_employee_button.pack()

        self.add_client_button = tk.Button(self.client_tab, text="Add Client", command=self.add_client_dialog)
        self.add_client_button.pack()

        self.add_supplier_button = tk.Button(self.supplier_tab, text="Add Supplier", command=self.add_supplier_dialog)
        self.add_supplier_button.pack()

        self.add_event_button = tk.Button(self.event_tab, text="Add Event", command=self.add_event_dialog)
        self.add_event_button.pack()

    def load_employees(self):
        # Load employees from file or database
        employees = []
        try:
            with open('employees.pkl', 'rb') as f:
                employees = pickle.load(f)
        except FileNotFoundError:
            pass

        for employee in employees:
            self.employee_table.insert('', 'end', values=(
            employee.name, employee.department, employee.job_title, employee.basic_salary))

    def add_employee_dialog(self):
        employee_info = self.get_employee_info()
        if employee_info:
            name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details = employee_info
            employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth,
                                passport_details)
            self.employee_table.insert('', 'end', values=(name, employee_id, department, job_title, basic_salary))

            # Save employee to file or database
            with open('employees.pkl', 'ab') as f:
                pickle.dump(employee, f)

    def get_employee_info(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Add Employee")

        tk.Label(dialog, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(dialog, text="ID:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Department:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Job Title:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Salary:").grid(row=4, column=0, padx=5, pady=5)

        name_entry = tk.Entry(dialog)
        id_entry = tk.Entry(dialog)
        department_entry = tk.Entry(dialog)
        job_title_entry = tk.Entry(dialog)
        salary_entry = tk.Entry(dialog)

        name_entry.grid(row=0, column=1, padx=5, pady=5)
        id_entry.grid(row=1, column=1, padx=5, pady=5)
        department_entry.grid(row=2, column=1, padx=5, pady=5)
        job_title_entry.grid(row=3, column=1, padx=5, pady=5)
        salary_entry.grid(row=4, column=1, padx=5, pady=5)

        ok_button = tk.Button(dialog, text="OK",
                              command=lambda: self.confirm_employee(dialog, name_entry.get(), id_entry.get(),
                                                                    department_entry.get(), job_title_entry.get(),
                                                                    salary_entry.get()))
        ok_button.grid(row=5, column=0, columnspan=2, pady=10)

        dialog.grab_set()
        dialog.wait_window()

    def confirm_employee(self, dialog, name, employee_id, department, job_title, salary):
        if name and employee_id and department and job_title and salary:
            employee = Employee(name, employee_id, department, job_title, salary, "", "", "")
            self.employee_info = (name, employee_id, department, job_title, salary)
            self.employee_table.insert('', 'end', values=(
                employee.name, employee.employee_id, employee.department, employee.job_title, employee.basic_salary))

            # Save employee to file or database
            with open('employees.pkl', 'ab') as f:
                pickle.dump(employee, f)

            dialog.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def load_clients(self):
        # Load clients from file or database
        clients = []
        try:
            with open('clients.pkl', 'rb') as f:
                clients = pickle.load(f)
                if not isinstance(clients, list):  # Ensure clients is a list
                    clients = [clients]  # Convert single client to a list
        except FileNotFoundError:
            pass

        for client in clients:
            self.client_table.insert('', 'end', values=(
                client.client_id, client.name, client.address, client.contact_details, client.budget))

    def add_client_dialog(self):
        client_info = self.get_client_info()
        if client_info:
            client = Client(*client_info)
            self.client_table.insert('', 'end', values=(
            client.client_id, client.name, client.address, client.contact_details, client.budget))

            # Save client to file or database
            with open('clients.pkl', 'ab') as f:
                pickle.dump(client, f)

    def get_client_info(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Add Client")

        tk.Label(dialog, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Budget:").grid(row=4, column=0, padx=5, pady=5)

        id_entry = tk.Entry(dialog)
        name_entry = tk.Entry(dialog)
        address_entry = tk.Entry(dialog)
        contact_details_entry = tk.Entry(dialog)
        budget_entry = tk.Entry(dialog)

        id_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        address_entry.grid(row=2, column=1, padx=5, pady=5)
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)
        budget_entry.grid(row=4, column=1, padx=5, pady=5)

        ok_button = tk.Button(dialog, text="OK",
                              command=lambda: self.confirm_client(dialog, id_entry.get(), name_entry.get(),
                                                                   address_entry.get(), contact_details_entry.get(),
                                                                   budget_entry.get()))
        ok_button.grid(row=5, column=0, columnspan=2, pady=10)

        dialog.grab_set()
        dialog.wait_window()

        return self.client_info

    def confirm_client(self, dialog, client_id, name, address, contact_details, budget):
        if client_id and name and address and contact_details and budget:
            self.client_info = (client_id, name, address, contact_details, budget)
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def load_suppliers(self):
        # Load suppliers from file or database
        suppliers = []
        try:
            with open('suppliers.pkl', 'rb') as f:
                suppliers = pickle.load(f)
        except FileNotFoundError:
            pass

        for supplier in suppliers:
            self.supplier_table.insert('', 'end', values=(
            supplier.supplier_id, supplier.name, supplier.address, supplier.contact_details))

    def add_supplier_dialog(self):
        supplier_info = self.get_supplier_info()
        if supplier_info:
            supplier = Supplier(*supplier_info)
            self.supplier_table.insert('', 'end', values=(
            supplier.supplier_id, supplier.name, supplier.address, supplier.contact_details))

            # Save supplier to file or database
            with open('suppliers.pkl', 'ab') as f:
                pickle.dump(supplier, f)

    def get_supplier_info(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Add Supplier")

        tk.Label(dialog, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)

        id_entry = tk.Entry(dialog)
        name_entry = tk.Entry(dialog)
        address_entry = tk.Entry(dialog)
        contact_details_entry = tk.Entry(dialog)

        id_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        address_entry.grid(row=2, column=1, padx=5, pady=5)
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        ok_button = tk.Button(dialog, text="OK",
                              command=lambda: self.confirm_supplier(dialog, id_entry.get(), name_entry.get(),
                                                                     address_entry.get(), contact_details_entry.get()))
        ok_button.grid(row=4, column=0, columnspan=2, pady=10)

        dialog.grab_set()
        dialog.wait_window()

        return self.supplier_info

    def confirm_supplier(self, dialog, supplier_id, name, address, contact_details):
        if supplier_id and name and address and contact_details:
            self.supplier_info = (supplier_id, name, address, contact_details)
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def load_events(self):
        # Load events from file or database
        events = []
        try:
            with open('events.pkl', 'rb') as f:
                events = pickle.load(f)
        except FileNotFoundError:
            pass

        for event in events:
            self.event_table.insert('', 'end', values=(
            event.event_id, event.event_type, event.theme, event.date, event.time, event.duration, event.venue_address,
            event.client))

    def add_event_dialog(self):
        event_info = self.get_event_info()
        if event_info:
            event = Event(*event_info)
            self.event_table.insert('', 'end', values=(
            event.event_id, event.event_type, event.theme, event.date, event.time, event.duration, event.venue_address,
            event.client))

            # Save event to file or database
            with open('events.pkl', 'ab') as f:
                pickle.dump(event, f)

    def get_event_info(self):
        dialog = tk.Toplevel(self.master)
        dialog.title("Add Event")

        tk.Label(dialog, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Theme:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Date:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Time:").grid(row=4, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Duration:").grid(row=5, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Venue:").grid(row=6, column=0, padx=5, pady=5)
        tk.Label(dialog, text="Client:").grid(row=7, column=0, padx=5, pady=5)

        id_entry = tk.Entry(dialog)
        type_entry = tk.Entry(dialog)
        theme_entry = tk.Entry(dialog)
        date_entry = tk.Entry(dialog)
        time_entry = tk.Entry(dialog)
        duration_entry = tk.Entry(dialog)
        venue_entry = tk.Entry(dialog)
        client_entry = tk.Entry(dialog)

        id_entry.grid(row=0, column=1, padx=5, pady=5)
        type_entry.grid(row=1, column=1, padx=5, pady=5)
        theme_entry.grid(row=2, column=1, padx=5, pady=5)
        date_entry.grid(row=3, column=1, padx=5, pady=5)
        time_entry.grid(row=4, column=1, padx=5, pady=5)
        duration_entry.grid(row=5, column=1, padx=5, pady=5)
        venue_entry.grid(row=6, column=1, padx=5, pady=5)
        client_entry.grid(row=7, column=1, padx=5, pady=5)

        ok_button = tk.Button(dialog, text="OK",
                              command=lambda: self.confirm_event(dialog, id_entry.get(), type_entry.get(),
                                                                  theme_entry.get(), date_entry.get(), time_entry.get(),
                                                                  duration_entry.get(), venue_entry.get(),
                                                                  client_entry.get()))
        ok_button.grid(row=8, column=0, columnspan=2, pady=10)

        dialog.grab_set()
        dialog.wait_window()

        return self.event_info

    def confirm_event(self, dialog, event_id, event_type, theme, date, time, duration, venue, client):
        if event_id and event_type and theme and date and time and duration and venue and client:
            self.event_info = (event_id, event_type, theme, date, time, duration, venue, client)
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")


root = tk.Tk()
app = EmployeeManagementApp(root)
root.mainloop()
