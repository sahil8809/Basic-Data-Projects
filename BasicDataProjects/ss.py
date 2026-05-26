with open ("students_record.txt","r") as file:
    data = file.read()
    name = input("Enter name: ").strip()
    if name in data:
        print("YES")
    else:
        print("NO")