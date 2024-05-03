
class Person:
    def __init__(self, name, age, date_of_birth, passport_details):
        self.name = name
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
# Getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_date_of_birth(self):
        return self._date_of_birth

    def get_passport_details(self):
        return self._passport_details

    # Setters
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def set_passport_details(self, passport_details):
        self._passport_details = passport_details


#----------------------------------------

class SalesManager(Person):
    def __init__(self, name, age, date_of_birth, passport_details, id_number, department, job_title, basic_salary):
        Person.__init__(self, name, age, date_of_birth, passport_details)
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary

# Getters
    def get_id_number(self):
        return self._id_number

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

    def get_basic_salary(self):
        return self._basic_salary

    # Setters
    def set_id_number(self, id_number):
        self._id_number = id_number

    def set_department(self, department):
        self._department = department

    def set_job_title(self, job_title):
        self._job_title = job_title

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

#----------------------------------------

class SalesPerson(Person):
    def __init__(self, name, age, date_of_birth, passport_details, id_number, department, job_title, basic_salary, manager_id):
        Person.__init__(self, name, age, date_of_birth, passport_details)
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.manager_id = manager_id

# Getters
    def get_id_number(self):
        return self._id_number

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

    def get_basic_salary(self):
        return self._basic_salary

    def get_manager_id(self):
        return self._manager_id

    # Setters
    def set_id_number(self, id_number):
        self._id_number = id_number

    def set_department(self, department):
        self._department = department

    def set_job_title(self, job_title):
        self._job_title = job_title

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

#----------------------------------------

class MarketingManager(Person):
    def __init__(self, name, age, date_of_birth, passport_details, id_number, department, job_title, basic_salary):
        Person.__init__(self, name, age, date_of_birth, passport_details)
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary

    # Getters
    def get_id_number(self):
        return self._id_number

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

    def get_basic_salary(self):
        return self._basic_salary

    # Setters
    def set_id_number(self, id_number):
        self._id_number = id_number

    def set_department(self, department):
        self._department = department

    def set_job_title(self, job_title):
        self._job_title = job_title

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

#----------------------------------------

class Marketer(Person):
    def __init__(self, name, age, date_of_birth, passport_details, id_number, department, job_title, basic_salary, manager_id):
        Person.__init__(self, name, age, date_of_birth, passport_details)
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.manager_id = manager_id

    def get_id_number(self):
        return self._id_number

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

    def get_basic_salary(self):
        return self._basic_salary

    def get_manager_id(self):
        return self._manager_id

    # Setters
    def set_id_number(self, id_number):
        self._id_number = id_number

    def set_department(self, department):
        self._department = department

    def set_job_title(self, job_title):
        self._job_title = job_title

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

#----------------------------------------

class Designer(Person):
    def __init__(self, name, age, date_of_birth, passport_details, id_number, department, job_title, basic_salary, manager_id):
        Person.__init__(self, name, age, date_of_birth, passport_details)
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.manager_id = manager_id

    # Getters
    def get_id_number(self):
        return self._id_number

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

    def get_basic_salary(self):
        return self._basic_salary

    def get_manager_id(self):
        return self._manager_id

    # Setters
    def set_id_number(self, id_number):
        self._id_number = id_number

    def set_department(self, department):
        self._department = department

    def set_job_title(self, job_title):
        self._job_title = job_title

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

#----------------------------------------
class Accountant(Person):
    def __init__(self, name, age, date_of_birth, passport_details, id_number, department, job_title, basic_salary, manager_id):
        Person.__init__(self, name, age, date_of_birth, passport_details)
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.manager_id = manager_id

    # Getters
    def get_id_number(self):
        return self._id_number

    def get_department(self):
        return self._department

    def get_job_title(self):
        return self._job_title

    def get_basic_salary(self):
        return self._basic_salary

    def get_manager_id(self):
        return self._manager_id

    # Setters
    def set_id_number(self, id_number):
        self._id_number = id_number

    def set_department(self, department):
        self._department = department

    def set_job_title(self, job_title):
        self._job_title = job_title

    def set_basic_salary(self, basic_salary):
        self._basic_salary = basic_salary

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id

#----------------------------------------
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    # Getters
    def get_client_id(self):
        return self._client_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    def get_budget(self):
        return self._budget

    # Setters
    def set_client_id(self, client_id):
        self._client_id = client_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    def set_budget(self, budget):
        self._budget = budget

#----------------------------------------
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Getters
    def get_supplier_id(self):
        return self._supplier_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

#----------------------------------------
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

    # Getters
    def get_event_id(self):
        return self._event_id

    def get_event_type(self):
        return self._event_type

    def get_theme(self):
        return self._theme

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_duration(self):
        return self._duration

    def get_venue_address(self):
        return self._venue_address

    def get_client(self):
        return self._client

    def get_guest_list(self):
        return self._guest_list

    def get_suppliers(self):
        return self._suppliers

    # Setters
    def set_event_id(self, event_id):
        self._event_id = event_id

    def set_event_type(self, event_type):
        self._event_type = event_type

    def set_theme(self, theme):
        self._theme = theme

    def set_date(self, date):
        self._date = date

    def set_time(self, time):
        self._time = time

    def set_duration(self, duration):
        self._duration = duration

    def set_venue_address(self, venue_address):
        self._venue_address = venue_address

    def set_client(self, client):
        self._client = client

    def set_guest_list(self, guest_list):
        self._guest_list = guest_list

    def set_suppliers(self, suppliers):
        self._suppliers = suppliers

    # Getters
    def get_company_id(self):
        return self._company_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_company_id(self, company_id):
        self._company_id = company_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

#----------------------------------------

class DecorationCompany:
    def __init__(self, company_id, name, address, contact_details):
        self.company_id = company_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Getters
    def get_company_id(self):
        return self._company_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_company_id(self, company_id):
        self._company_id = company_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

#----------------------------------------
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Getters
    def get_guest_id(self):
        return self._guest_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_guest_id(self, guest_id):
        self._guest_id = guest_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

#----------------------------------------
class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Getters
    def get_venue_id(self):
        return self._venue_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact(self):
        return self._contact

    def get_min_guests(self):
        return self._min_guests

    def get_max_guests(self):
        return self._max_guests

    # Setters
    def set_venue_id(self, venue_id):
        self._venue_id = venue_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact(self, contact):
        self._contact = contact

    def set_min_guests(self, min_guests):
        self._min_guests = min_guests

    def set_max_guests(self, max_guests):
        self._max_guests = max_guests

#----------------------------------------
class CleaningCompany:
    def __init__(self, company_id, name, address, contact_details):
        self.company_id = company_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Getters
    def get_company_id(self):
        return self._company_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_company_id(self, company_id):
        self._company_id = company_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

#----------------------------------------
class EntertainmentCompany:
    def __init__(self, company_id, name, address, contact_details):
        self.company_id = company_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

   # Getters
    def get_company_id(self):
        return self._company_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_company_id(self, company_id):
        self._company_id = company_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

#----------------------------------------
class FurnitureCompany:
    def __init__(self, company_id, name, address, contact_details):
        self.company_id = company_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Getters
    def get_company_id(self):
        return self._company_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    # Setters
    def set_company_id(self, company_id):
        self._company_id = company_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

#----------------------------------------
class Caterer:
    def __init__(self, caterer_id, name, address, contact_details, menu):
        self.caterer_id = caterer_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
    # Getters
    def get_caterer_id(self):
        return self._caterer_id

    def get_name(self):
        return self._name

    def get_address(self):
        return self._address

    def get_contact_details(self):
        return self._contact_details

    def get_menu(self):
        return self._menu

    # Setters
    def set_caterer_id(self, caterer_id):
        self._caterer_id = caterer_id

    def set_name(self, name):
        self._name = name

    def set_address(self, address):
        self._address = address

    def set_contact_details(self, contact_details):
        self._contact_details = contact_details

    def set_menu(self, menu):
        self._menu = menu


#----------------------------------------

# example objects (some using the table provided):
sm1 = SalesManager("Susan Meyers", 45, "22-03-1979", "AB3456", 47899, "Sales", "Manager", 37500)
sm2= SalesManager("joy Rogers", 41, "08-02-1983", "A123487", 81774, "Sales", "Manager", 24000)

sp1 = SalesPerson("Shyam Sundar", 30, "15-06-1994", "BC9654", 22334, "Sales", "Salesperson", 20000, 47899)
sp2 = SalesPerson("Mariam Khalid", 29, "05-05-1995", "AC8765", 22344, "Sales", "Salesperson", 20000, 81774)

mm1 = MarketingManager("Meera Mohamed", 41, "19-06-1983", "MNO56989", 44556, "Marketing", "Manager", 31000)
d1 = Designer("Amna Abdulla", 33, "27-05-1991", "DEF35678", 44566, "Design", "Designer", 29000, 11223)

print("Sales Manager:")
print("Name:", sm1.name)
print("Age:", sm1.age)
print("Date of Birth:", sm1.date_of_birth)
print("Passport Details:", sm1.passport_details)
print("Employee ID:", sm1.id_number)
print("Department:", sm1.department)
print("Job Title:", sm1.job_title)
print("Basic Salary:", sm1.basic_salary)
print()

print("Sales Person:")
print("Name:", sp1.name)
print("Age:", sp1.age)
print("Date of Birth:", sp1.date_of_birth)
print("Passport Details:", sp1.passport_details)
print("Employee ID:", sp1.id_number)
print("Department:", sp1.department)
print("Job Title:", sp1.job_title)
print("Basic Salary:", sp1.basic_salary)
print("Manager ID:", sp1.manager_id)
print()

print("Marketing Manager:")
print("Name:", mm1.name)
print("Age:", mm1.age)
print("Date of Birth:", mm1.date_of_birth)
print("Passport Details:", mm1.passport_details)
print("Employee ID:", mm1.id_number)
print("Department:", mm1.department)
print("Job Title:", mm1.job_title)
print("Basic Salary:", mm1.basic_salary)
print()

print("Designer:")
print("Name:", d1.name)
print("Age:", d1.age)
print("Date of Birth:", d1.date_of_birth)
print("Passport Details:", d1.passport_details)
print("Employee ID:", d1.id_number)
print("Department:", d1.department)
print("Job Title:", d1.job_title)
print("Basic Salary:", d1.basic_salary)
print("Manager ID:", d1.manager_id)
