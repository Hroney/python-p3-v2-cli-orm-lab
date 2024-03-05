from models.department import Department
from models.employee import Employee
import os

def exit_program():
    print("Goodbye!")
    exit()

def clear():
    os.system('cls||clear')

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)
    pass


def find_employee_by_name():
    name = input("Please enter the name of the Employee: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f'{name} is not an employee / not found.')


def find_employee_by_id():
    id_ = input("Enter the ID of the Employee: ")
    employee = Employee.find_by_id(id_)
    print(employee)


def create_employee():
    name = input("Enter the Employee's name: ")
    job_title = input("Enter the Employee's Job Title: ")
    department_id = int(input("Enter the Employee's Department ID: "))
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id_ = input("Enter the Employee's id: ")
    if employee := Employee.find_by_id(id_):
        print(employee)
        print("Choose Update Field")
        print("1: Update Name")
        print("2: Update Job Title")
        print("3: Update Department")
        choice = input("> ")
        try:
            if choice == "1":
                name = input("Enter the Employee's new name: ")
                employee.name = name
            if choice == "2":
                job_title = input("Enter the Employee's new Job Title: ")
                employee.job_title = job_title
            if choice == "3":
                department_id = input("Enter the Employee's new Department ID: ")
                employee.department_id = department_id
            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')


def delete_employee():
    list_employees()
    id_ = input("Enter the Employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    id_ = input("Enter the Department ID: ")
    if department := Department.find_by_id(id_):
        try:
            for employee in Employee.get_all():
                if employee.department_id == department.id:
                    print(employee)
        except Exception as exc:
            print(f'Error looking up Employees: ', exc)
    else:
        print(f'Department {id_} not found')
        