# Hospital Management System
# Name: Samiksha Pramod Denge
# USN: CD25040

patients = {}
doctors = {}
rooms = {}
resources = {}
bills = {}

def add_patient():
    pid = input("Patient ID: ")
    patients[pid] = {
        "name": input("Name: "),
        "age": input("Age: "),
        "disease": input("Disease: ")
    }
    print("Patient added!")

def view_patients():
    print(patients)

def add_doctor():
    did = input("Doctor ID: ")
    doctors[did] = {
        "name": input("Name: "),
        "specialization": input("Specialization: ")
    }
    print("Doctor added!")

def view_doctors():
    print(doctors)

def add_room():
    r = input("Room Number: ")
    rooms[r] = input("Room Type: ")
    print("Room added!")

def add_resource():
    r = input("Resource Name: ")
    resources[r] = int(input("Quantity: "))
    print("Resource added!")

def generate_bill():
    pid = input("Patient ID: ")
    amount = float(input("Enter Bill Amount: "))
    bills[pid] = amount
    print("Total Bill:", amount)

while True:
    print("""
--- HOSPITAL MANAGEMENT ---
1. Add Patient
2. View Patients
3. Add Doctor
4. View Doctors
5. Add Room
6. Add Resource
7. Generate Bill
8. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        add_doctor()
    elif choice == "4":
        view_doctors()
    elif choice == "5":
        add_room()
    elif choice == "6":
        add_resource()
    elif choice == "7":
        generate_bill()
    elif choice == "8":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
