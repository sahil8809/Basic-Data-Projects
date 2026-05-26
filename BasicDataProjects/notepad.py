# def write_note():
#     notes = input("Enter note : ")
#     with open("notes.txt","a") as file:
#         file.write(notes + "\n")
#     print("notes saved!")

# def read_note():
#     print("Your note...")
#     with open("notes.txt","r") as file:
#         for i in file:
#             print(i.strip())

# write_note()
# read_note()

from grades import grade
grade()