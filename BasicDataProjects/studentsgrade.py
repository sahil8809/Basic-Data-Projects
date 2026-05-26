# def grade():
#     subjects = ["math","physics","chemistry","english"]
#     name = input("Enter your name: ")
#     marks_dict = {}
#     for s in subjects:
#         marks = float(input(f"Enter marks {s}:"))
#         marks_dict[s]=marks
#     failed = []
#     for sub, marks in marks_dict.items():
#         if marks < 30:
#             failed.append(sub)
#             print(f"{name} failed in {failed}")
#             break
    
    
        
#     total = sum(marks_dict.values())
#     percent = total/len(subjects)

#     print(f"marks in percentage: {percent}%")

#     if percent < 0 or percent >100:
#         print("Marks should be b/w 0 to 100")
#     elif percent >= 90:
#         print(f"{name} - Grade : A")
#     elif percent >=75:
#         print(f'{name} - Grade : B')
#     elif percent >=60:
#         print(f"{name} - Grade : C")
#     elif percent >= 30:
#         print(f"{name} - Grade : D")
#     elif percent < 30 and percent >=0:
#         print(f"{name} - fail")
        
# grade()


def grade():
    subjects = ["math", "physics", "chemistry", "english"]
    
    name = input("Enter your name: ")
    
    marks_dict = {}

    for s in subjects:
        marks = float(input(f"Enter marks {s}: "))
        if marks > 100 or marks < 0:
            print("marks should be b/t 0 to 100")
            return
        marks_dict[s] = marks

    failed = []

    for sub, marks in marks_dict.items():
        if marks < 30:
            failed.append(sub)

    if failed:
        result = print(f"{name} failed in: {', '.join(failed)}")
        return
        with open("data_of_students","a") as file:
            file.write(result +"\n")

    total = sum(marks_dict.values())
    percent = total / len(subjects)

    final_result = print(f"{name} | marks percentage: {percent}%")

    if percent < 0 or percent > 100:
        print("Marks should be b/w 0 to 100")
    elif percent >= 90:
        print(f"{name} - Grade : A")
    elif percent >= 75:
        print(f"{name} - Grade : B")
    elif percent >= 60:
        print(f"{name} - Grade : C")
    elif percent >= 30:
        print(f"{name} - Grade : D")
    with open("data_of_students.txt","a") as f:
        f.write(final_result + "\n")

grade()