patients={}
appointments=[]

while True:
    print("\n1.Add Patient\n2.View Patients\n3.Book Appointment\n4.Generate Bill\n5.Exit")
    ch=input("Enter choice: ")

    if ch=="1":
        pid=input("Patient ID: ")
        name=input("Name: ")
        age=input("Age: ")
        disease=input("Disease: ")
        patients[pid]= {"name":name,"age":age,"disease":disease}

    elif ch=="2":
        for p in patients:
            print(p,patients[p])

    elif ch=="3":
        pid=input("Patient ID: ")
        if pid in patients:
            doctor=input("Doctor: ")
            appointments.append((pid,doctor))
            print("Appointment booked")
        else:
            print("Patient not found")

    elif ch=="4":
        pid=input("Patient ID: ")
        consult=int(input("Consultation: "))
        med=int(input("Medication: "))
        print("Total Bill:",consult+med)

    elif ch=="5":
        break
