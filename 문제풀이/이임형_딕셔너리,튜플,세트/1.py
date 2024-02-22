students=[
    {"name":'hong','korean':87,'math':98,'english':88,'science': 95},
{"name":'lee','korean':92,'math':98,'english':96,'science': 98},
{"name":'sung','korean':76,'math':96,'english':94,'science': 90},
{"name":'byeon','korean':98,'math':92,'english':96,'science': 92},
{"name":'park','korean':95,'math':98,'english':98,'science': 98},
{"name":'ryu','korean':64,'math':88,'english':92,'science': 92},
]

print(f'{"이름":<5}{"총점":<5}{"평균":>5}')

for student in students:
    name=student['name']
    total=0
    for i in student.values():
        if type(i)==int:
            total+=i

    avg=total/(len(student)-1)
    print(f'{name:<5}{total:<5}{avg:>5.2f}')