from chair import Chair

chair_list = [
    Chair(),
    Chair.get_instance(),
    Chair(2, "Plastic", 100, "Bob")
]

for _ in chair_list:
    print(_)

arr = [i for i in range(1, 11)]

for i in arr:
    print(i)

for i in arr[::2]:
    print(i)

