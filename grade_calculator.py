name = input("Enter Student name: ")

math = int(input("Enter Math marks: "))
english = int(input("Enter English marks: "))
python = int(input("Enter Python marks: "))

if math > 100 or math < 0:
  print("Your Math Mark is Invalid")

if english > 100 or english < 0:
  print("Your English Mark is Invalid")

if python > 100 or python < 0:
  print("Your Python Mark is Invalid")

average_mark = (math + english + python) / 3

if average_mark >= 80 and average_mark <= 100:
  final_grade = "A+"
elif average_mark >= 70 and average_mark <= 79:
  final_grade = "A"
elif average_mark >= 60 and average_mark <= 69:
  final_grade = "A-"
elif average_mark >= 50 and average_mark <= 59:
  final_grade = "B"
elif average_mark >= 40 and average_mark <= 49:
  final_grade = "C"
elif average_mark >= 0 and average_mark < 40:
  final_grade = "F"
else:
  final_grade = ":("

print(f"Student Name: {name}")
print(f"Average Mark: {average_mark}")
print(f"Final Grade: {final_grade}")