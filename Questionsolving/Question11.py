#Student Grade Filter (using filter())
students = [
    {"name": "Ram", "age": 20, "grade": 90},
    {"name": "Sam", "age": 21, "grade": 96},
    {"name": "John", "age": 19, "grade": 98}
]

result = list(filter(lambda x: x["grade"] >= 95, students))

print(result)