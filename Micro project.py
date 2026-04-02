# Simple Hospital Management System

patients = {}
appointments = {}

def add_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")

    patients[pid] = {
        "name": name,
        "age": age,
        "disease": disease
    }
    print("Patient added successfully!")

def view_patients():
    if not patients:
        print("No patients found.")
        return

    for pid, details in patients.items():
        print(f"\nID: {pid}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Disease: {details['disease']}")

def search_patient():
    pid = input("Enter Patient ID to search: ")
    if pid in patients:
        p = patients[pid]
        print(f"Name: {p['name']}, Age: {p['age']}, Disease: {p['disease']}")
    else:
        print("Patient not found.")

def delete_patient():
    pid = input("Enter Patient ID to delete: ")
    if pid in patients:
        del patients[pid]
        print("Patient deleted.")
    else:
        print("Patient not found.")

def update_patient():
    pid = input("Enter Patient ID to update: ")
    if pid in patients:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        disease = input("Enter new disease: ")

        patients[pid] = {
            "name": name,
            "age": age,
            "disease": disease
        }
        print("Patient updated.")
    else:
        print("Patient not found.")

def add_appointment():
    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("Patient not found.")
        return

    date = input("Enter Appointment Date: ")
    doctor = input("Enter Doctor Name: ")

    appointments[pid] = {
        "date": date,
        "doctor": doctor
    }
    print("Appointment added.")

def view_appointments():
    if not appointments:
        print("No appointments found.")
        return

    for pid, details in appointments.items():
        print(f"\nPatient ID: {pid}")
        print(f"Date: {details['date']}")
        print(f"Doctor: {details['doctor']}")

def generate_bill():
    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("Patient not found.")
        return

    print("\n--- BILL ---")
    print(f"Patient Name: {patients[pid]['name']}")

    consultation = float(input("Consultation Fee: "))
    medicine = float(input("Medicine Charges: "))
    total = consultation + medicine

    print(f"Total Bill: ₹{total}")

# Main Menu
while True:
    print("\n===== HOSPITAL MENU =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Update Patient")
    print("6. Add Appointment")
    print("7. View Appointments")
    print("8. Generate Bill")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        delete_patient()
    elif choice == "5":
        update_patient()
    elif choice == "6":
        add_appointment()
    elif choice == "7":
        view_appointments()
    elif choice == "8":
        generate_bill()
    elif choice == "9":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
import tkinter as tk
from tkinter import messagebox

patients = {}

# Functions
def add_patient():
    pid = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    disease = entry_disease.get()

    if pid == "":
        messagebox.showerror("Error", "Patient ID required")
        return

    patients[pid] = {"name": name, "age": age, "disease": disease}
    messagebox.showinfo("Success", "Patient Added")

def view_patients():
    output.delete("1.0", tk.END)
    if not patients:
        output.insert(tk.END, "No patients found\n")
        return

    for pid, p in patients.items():
        output.insert(tk.END,
            f"ID: {pid}\nName: {p['name']}\nAge: {p['age']}\nDisease: {p['disease']}\n\n"
        )

def search_patient():
    pid = entry_id.get()
    output.delete("1.0", tk.END)

    if pid in patients:
        p = patients[pid]
        output.insert(tk.END,
            f"Name: {p['name']}\nAge: {p['age']}\nDisease: {p['disease']}"
        )
    else:
        output.insert(tk.END, "Patient not found")

def delete_patient():
    pid = entry_id.get()
    if pid in patients:
        del patients[pid]
        messagebox.showinfo("Deleted", "Patient removed")
    else:
        messagebox.showerror("Error", "Patient not found")

