
student_name = input("Enter student name : ")
tamil_mark = int(input("Enter Tamil Mark : "))
English_mark = int(input("Enter English Mark : "))
Maths_mark = int(input("Enter Maths Mark : "))
Science_mark = int(input("Enter Science Mark : "))
Computer_mark = int(input("Enter Computer Mark : "))

total_mark = tamil_mark + English_mark + Maths_mark + Science_mark + Computer_mark
average = total_mark/5

match average:
    case average if average > 90:
        grade = "A"
    case average if average > 80:
        grade = "B"
    case average if average > 60:
        grade = "C"
    case average if average > 40:
        grade = "D"
    case _:
        grade = "F"


if(tamil_mark > 35 and English_mark > 35 and Maths_mark > 35 and Science_mark > 35 and Computer_mark > 35):
    result = "PASS"
else:
    result = "FAIL"



print("\nStudent Result ")
print("Student Name:", student_name)
print("Tamil :", tamil_mark)
print("English :", English_mark)
print("Maths :", Maths_mark)
print("Science :", Science_mark)
print("Computer :", Computer_mark)

print("Total:", total_mark)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)








# student_name=input("Enter student name: ")

# marks = []
# for i in range(1,6):
#     mark = int(input(f"Enter mark of subject: {i}"))
#     marks.append(mark)

# total = sum(marks)
# average = total/5


# if all(mark >= 35 for mark in marks):
#     result = "Pass"
# else:
#     result = "Fail"

# if result == "Pass":
#     match average:
#         case average if average > 90:
#             grade = "A"
#         case average if average > 80:
#             grade = "B"
#         case average if average > 60:
#             grade = "C"
#         case average if average > 40:
#             grade = "D"
#         case _:
#             grade = "F"

# else:
#     grade = "Fail"



# print("\nStudent Result ")
# print("Student Name:", student_name)
# print("Marks:", marks)
# print("Total:", total)
# print("Average:", average)
# print("Grade:", grade)
# print("Result:", result)


