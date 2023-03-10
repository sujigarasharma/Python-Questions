
num_subjects = int(input(f"Enter the Number of subjects: "))

grades = []
credits = []

for i in range(num_subjects):
    grade = float(input(f"Enter grade obtained in subject {i+1}: "))
    credit = int(input(f"Enter credit for subject {i+1}: "))
    grades.append(grade)
    credits.append(credit)

total_credits = sum(credits)
weighted_sum = sum([grades[i]*credits[i] for i in range(num_subjects)])
gpa = weighted_sum/total_credits

print(f"The GPA for this semester is: {gpa:.2f}")
