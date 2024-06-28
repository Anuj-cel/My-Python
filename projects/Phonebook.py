phonebook={}

print("Welcome to PYTHON Phonebook")
print("Facilities available ")
print("1. Add name and number ")
print("2. Edit name or number ")
print("3. Delete name and number ")
print("4. Delete name and number ")
print("5. Exit ")
choice =input("Enter your choice ")
while(1):
    if(choice=="1"):
        name=input("Enter name : ")
        phone_number=input("Enter phone number : ")
        phonebook[name]=phone_number
    elif(choice=="2"):
        name=input("Enter name : ")
        phone_number=input("Enter phone number : ")
        phonebook[name]=phone_number
    elif(choice=="3"):
        name=input("Enter name : ")
        phonebook.__delitem__(name)
    elif(choice=="4"):
        print("Name PhoneNumber")
        for item in phonebook:
            print(f"{item} -> {phonebook[item]}")
    elif(choice=="5"):
        break
    else:
        print("Invalid choice ")
    choice =input("Enter your choice ")
    

