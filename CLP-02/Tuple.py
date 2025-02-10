
students = (
    ("Salah uddin", 20, 85),
    ("Nayan", 22, 78),
    ("Rion", 21, 92),
    ("khaled", 23, 88),
    ("Fahad", 20, 95)
)

sorted_students = tuple(sorted(students, key=lambda x: x[2]))

print(sorted_students)
