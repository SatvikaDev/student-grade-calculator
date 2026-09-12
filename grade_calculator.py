print("Student Grade Calculator")

total = 0
for i in range(1,6):
    marks = float(input(f"Enter marks for subject{i} out of 100: "))
    total += marks
avg = total/5

#Grade
if avg >= 90:
    print("Grade-A")
elif avg >= 75:
    print("Grade-B")
elif avg >= 60:
    print("Grade-C")
elif avg >= 40:
    print("Grade-D")
else:
    print("Fail")