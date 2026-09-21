# Hospital Resource & Patient Management System
# Project ID: CD25040
# Name: Samiksha Pramod Denge
# USN: CD25040

patients = {}
doctors = {}
rooms = {}
resources = {}
bills = {}
treatments = {}


def add_patient():
    pid = input("Enter Patient ID: ")

    if pid in patients:
        print("Patient already exists!")
        return

    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    phone = input("Enter Phone Number: ")

    patients[pid] = {
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "phone": phone
    }

    print("Patient added successfully!")


def view_patients():
    if not patients:
        print("No patient records found.")
        return

    print("\n----- Patient Records -----")

    for pid, data in patients.items():
        print("\nPatient ID:", pid)
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Gender:", data["gender"])
        print("Disease:", data["disease"])
        print("Phone:", data["phone"])


def add_doctor():
    did = input("Enter Doctor ID: ")

    if did in doctors:
        print("Doctor already exists!")
        return

    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    schedule = input("Enter Available Schedule: ")

    doctors[did] = {
        "name": name,
        "specialization": specialization,
        "schedule": schedule
    }

    print("Doctor added successfully!")


def view_doctors():
    if not doctors:
        print("No doctor records found.")
        return

    print("\n----- Doctor Records -----")

    for did, data in doctors.items():
        print("\nDoctor ID:", did)
        print("Name:", data["name"])
        print("Specialization:", data["specialization"])
        print("Schedule:", data["schedule"])


def book_appointment():
    pid = input("Enter Patient ID: ")
    did = input("Enter Doctor ID: ")

    if pid not in patients:
        print("Patient not found!")
        return

    if did not in doctors:
        print("Doctor not found!")
        return

    date = input("Enter Appointment Date: ")
    time = input("Enter Appointment Time: ")

    patients[pid]["appointment"] = {
        "doctor": doctors[did]["name"],
        "date": date,
        "time": time
    }

    print("Appointment booked successfully!")


def add_room():
    room_no = input("Enter Room Number: ")

    if room_no in rooms:
        print("Room already exists!")
        return

    room_type = input("Enter Room Type (General/ICU/Private): ")

    rooms[room_no] = {
        "type": room_type,
        "occupied": False,
        "patient": None
    }

    print("Room added successfully!")


def allocate_room():
    room_no = input("Enter Room Number: ")
    pid = input("Enter Patient ID: ")

    if room_no not in rooms:
        print("Room not found!")
        return

    if pid not in patients:
        print("Patient not found!")
        return

    if rooms[room_no]["occupied"]:
        print("Room is already occupied!")
        return

    rooms[room_no]["occupied"] = True
    rooms[room_no]["patient"] = pid

    print("Room allocated successfully!")


def view_rooms():
    if not rooms:
        print("No rooms available.")
        return

    print("\n----- Room Details -----")

    for room, data in rooms.items():
        print("\nRoom:", room)
        print("Type:", data["type"])

        if data["occupied"]:
            print("Status: Occupied")
            print("Patient ID:", data["patient"])
        else:
            print("Status: Available")


def add_resource():
    resource = input("Enter Resource Name: ")
    quantity = int(input("Enter Quantity: "))

    resources[resource] = resources.get(resource, 0) + quantity

    print("Resource added successfully!")


def view_resources():
    if not resources:
        print("No medical resources found.")
        return

    print("\n----- Medical Resources -----")

    for resource, quantity in resources.items():
        print(resource, ":", quantity)


def add_treatment():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return

    treatment = input("Enter Treatment/Medicine: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Date: ")

    if pid not in treatments:
        treatments[pid] = []

    treatments[pid].append({
        "treatment": treatment,
        "doctor": doctor,
        "date": date
    })

    print("Treatment history added successfully!")


def view_treatment():
    pid = input("Enter Patient ID: ")

    if pid not in treatments:
        print("No treatment history found.")
        return

    print("\n----- Treatment History -----")

    for record in treatments[pid]:
        print("\nDate:", record["date"])
        print("Doctor:", record["doctor"])
        print("Treatment:", record["treatment"])


def generate_bill():
    pid = input("Enter Patient ID: ")

    if pid not in patients:
        print("Patient not found!")
        return

    room_charge = float(input("Enter Room Charges: "))
    doctor_charge = float(input("Enter Doctor Charges: "))
    medicine_charge = float(input("Enter Medicine Charges: "))
    other_charge = float(input("Enter Other Charges: "))

    total = room_charge + doctor_charge + medicine_charge + other_charge

    bills[pid] = {
        "room": room_charge,
        "doctor": doctor_charge,
        "medicine": medicine_charge,
        "other": other_charge,
        "total": total
    }

    print("\n----- BILL -----")
    print("Patient:", patients[pid]["name"])
    print("Room Charges:", room_charge)
    print("Doctor Charges:", doctor_charge)
    print("Medicine Charges:", medicine_charge)
    print("Other Charges:", other_charge)
    print("Total Bill:", total)


def main():
    while True:
        print("\n========================================")
        print(" HOSPITAL RESOURCE & PATIENT MANAGEMENT")
        print("========================================")

        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. Add Room")
        print("7. Allocate Room")
        print("8. View Rooms")
        print("9. Add Medical Resource")
        print("10. View Medical Resources")
        print("11. Add Treatment History")
        print("12. View Treatment History")
        print("13. Generate Bill")
        print("14. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            add_doctor()
        elif choice == "4":
            view_doctors()
        elif choice == "5":
            book_appointment()
        elif choice == "6":
            add_room()
        elif choice == "7":
            allocate_room()
        elif choice == "8":
            view_rooms()
        elif choice == "9":
            add_resource()
        elif choice == "10":
            view_resources()
        elif choice == "11":
            add_treatment()
        elif choice == "12":
            view_treatment()
        elif choice == "13":
            generate_bill()
        elif choice == "14":
            print("Thank you for using Hospital Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
