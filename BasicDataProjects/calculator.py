# # def calculator():
# #     while True:
# #         try:
# #             op = input("enter operator (+, -, *, /, //, **, exit) : ")
# #             if op == 'exit':
# #                 print("program ended!")
# #                 break

# #             if op not in ['+','-','*','**','/','//','exit']:  #checking operator is valid or not 
# #                 raise ValueError ("Invalid operator...! type correct operator")
# #             try:
# #                 num1 = int(input("Enter first number :"))
# #                 num2 = int(input("Enter second number :"))
# #             except ValueError:
# #                 print("Invalid input number")
# #                 continue

# #             if op == '+':
# #                 print ("Result : ",num1+num2)
# #             elif op == '-':
# #                 print("Result : ",num1-num2)
# #             elif op == '*':
# #                 print ("Result : ",num1*num2)
# #             elif op == '/':
# #                 try:
# #                     print("Result : ",num1/num2)
# #                 except ZeroDivisionError:
# #                     print("Cannot divide by zero!")
# #             elif op == '//':
# #                 try:
# #                     print("result : ", num1//num2)
# #                 except ZeroDivisionError:
# #                     print("Cannot divide by zero!")
            
# #             elif op == '**':
# #                 print("Result : ",num1**num2)

# #         except Exception as v:
# #             print(v)
# #         finally:
# #             print(20*"-","Calculation done",20*"-")
        
# # calculator()


def calculator():
    while True:
        op = input("Enter operator (+, -, *, /, //, **, exit): ")

        if op == 'exit':
            print("Program ended!")
            break

        if op not in ['+', '-', '*', '/', '//', '**']:
            print("Invalid operator...! Type correct operator")
            continue

        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input number")
            continue

        try:
            if op == '+':
                print("Result:",num1 + num2)
            elif op == '-':
                print("result:", num1 - num2)
            elif op == '*':
                print("Result:",num1 * num2)
            elif op == '/':
                print("result:", num1 / num2)
            elif op == '//':
                print("Result:",num1 // num2)
            elif op == '**':
                print("Result:",num1 ** num2)

        except ZeroDivisionError:
            print("Cannot divide by zero!")

        print("-" * 20, "Calculation done", "-" *20)

calculator()
