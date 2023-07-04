from json import load, dump

with open("data.json") as data:
    course = load(data)
    print(f"Nazwa {course['name']}")
    print("zapisani kursanci")
    for member in course['members']:
        print(f'- {member["first_name"]} {member["last_name"]}')

    first_name = input("imie:")
    last_name = input("Nazwisko:")

    with open("data.json", "w") as data:
        course['members'].append({
            "id": len(course['members'])+1,
            "first_name": first_name,
            "last_name": last_name
        })
        dump(course, data)