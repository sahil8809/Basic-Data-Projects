
def add_expense():
    Date = input("Enter date (DD-MM-YY): ").strip()
    try:
        amount =input("Enter amount: ")
    except ValueError:
        print("Invalid amount!")
        return
    
    purpose = input("Enter purpose: ").strip()

    with open("expenses.txt","a") as file:
        file.write(f"{Date}, {amount}, {purpose}\n")
    print("Expense saved!")

def show_expense():
    print ("_______All expenses______")
    try:
        with open ("expenses.txt","r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("file not existed")

add_expense()
show_expense()