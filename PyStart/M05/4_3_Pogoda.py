from urllib.request import urlopen
from json import loads
URL = "https://danepubliczne.imgw.pl/api/data/synop/"

with urlopen(URL) as file:
    data = loads(file.read().decode("utf-8"))
    # print(data)
    city = input("Lokalizacja: ")
    info = [row for row in data if row["stacja"] == city]
    info2 = list(filter(lambda x: x["stacja"] == city, data))
    if len(info2) == 0:
        print("nie wiem")
    else:
        temperature = info2[0]["temperatura"]
        pressure = info2[0]["cisnienie"]

        print(temperature, pressure)



"""
envPyStart\Scripts\activate.bat

"""
















