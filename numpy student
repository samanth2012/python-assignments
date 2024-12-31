import numpy as np

students = np.array([
    (19001, "Aarav", "CSE", "ECE", 95),
    (19002, "Ishaan", "MECH", "EEE", 89),
    (19003, "Ananya", "CSE", "EEE", 78),
    (19004, "Aditya", "EEE", "MECH", 92),
    (19005, "Diya", "ECE", "CSE", 88),
    (19006, "Rohan", "EEE", "CSE", 91),
    (19007, "Saanvi", "CSE", "MECH", 70),
    (19008, "Kavya", "MECH", "CSE", 65),
    (19009, "Vivaan", "EEE", "ECE", 85),
    (19010, "Arjun", "CSE", "MECH", 75),
    (19011, "Shivani", "ECE", "CSE", 79),
    (19012, "Isha", "CSE", "EEE", 80),
    (19013, "Krishna", "EEE", "ECE", 96),
    (19014, "Madhav", "MECH", "EEE", 86),
    (19015, "Reyansh", "CSE", "EEE", 82),
    (19016, "Tanvi", "ECE", "MECH", 64),
    (19017, "Rishi", "CSE", "MECH", 78),
    (19018, "Kiran", "EEE", "CSE", 90),
    (19019, "Pooja", "MECH", "CSE", 68),
    (19020, "Yash", "CSE", "EEE", 93)
], dtype=[("admission_number", "i4"), ("name", "U10"), ("department1", "U10"), ("department2", "U10"), ("total_marks", "i4")])

department_seats = {'CSE': 4, 'EEE': 4, 'ECE': 4, 'MECH': 4}
department_count = {'CSE': 0, 'EEE': 0, 'ECE': 0, 'MECH': 0}
assigned_students = {'CSE': [], 'EEE': [], 'ECE': [], 'MECH': []}
sorted_students = np.sort(students, order='total_marks')[::-1]

for student in sorted_students:
    if student['total_marks'] > 90:
        department = student['department1']
    elif 80 <= student['total_marks'] <= 90:
        department = student['department2']
    else:
        department = student['department1']

    if department_count[department] < department_seats[department]:
        assigned_students[department].append(student)
        department_count[department] += 1
    elif len(assigned_students[student['department2']]) < department_seats[student['department2']]:
        assigned_students[student['department2']].append(student)
        print("hello", student['name'], "assigned to", student['department2'])

print("Assigned Students to Departments:\n")
for department in assigned_students:
    print(f"{department} Department:")
    for student in assigned_students[department]:
        print(f" - {student['name']} (Admission No: {student['admission_number']}, Marks: {student['total_marks']})")
