def grade():
    subjects = ["math", "physics", "chemistry", "english"]

    name = input("Enter your name: ")

    marks_dict = {}

    for s in subjects:
        marks = float(input(f"Enter marks of {s}: "))

        if marks > 100 or marks < 0:
            print("Marks should be b/w 0 to 100")
            return

        marks_dict[s] = marks

    failed = []

    for sub, marks in marks_dict.items():
        if marks < 30:
            failed.append(sub)

    if failed:
        result = f"{name} |failed in -> {', '.join(failed)}"

        print(result)

        with open("students_record.txt", "a") as file:
            file.write(result + "\n")

            return

    total = sum(marks_dict.values())
    percent = total / len(subjects)

    if percent >= 90:
        grade = "A"

    elif percent >= 75:
        grade = "B"

    elif percent >= 60:
        grade= "C"

    else:
        grade = "D"

    result = (f"name: {name} | Percentage: {percent:.2f}% | Grade: {grade}")

    print(result)

    with open("students_record.txt", "a") as file:
        file.write(result + "\n")


grade()