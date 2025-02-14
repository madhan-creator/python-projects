# Get input for five subject marks
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / len(marks)

# Check average mark
if average < 35:
    print("Additional class is required.")
else:
    print("You are good to go.")
