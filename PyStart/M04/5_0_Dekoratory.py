"""
*args - wywolane argumenty nie nazwane
**kwargs - wywolane argumenty nazwane

"""
# przyklad 1
"""
def to_string(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        if isinstance(value, list):
            return [str(element) for element in value]
        else:
            return str(value)
        return wrapper
        
    # szablon
    def format_to_csv(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
        
        
"""
def format_to_csv(function):
    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs) # dostaje slownik
        if len(result) == 0:
            return ""
        keys = result[0].keys()
        output = [";".join(keys)] # [imie;nazwisko]

        for row in result:
            output.append(";".join(row.values()))
        return "\n".join(output)

    return wrapper

def test_format_to_csv():
    @format_to_csv
    def return_dict():
        return [
            {
                "imie": "Stefan",
                "nazwisko": "Zeromski"
            },
            {
                "imie": "Wladyslaw",
                "nazwisko": "Reymont"
            }
        ]
    result = return_dict()
    print(result)

    assert result == "imie;nazwisko\nStefan;Zeromski\nWladyslaw;Reymont"

"""
format_to_csv(return_dict)() # zapis dekoratora bez malpy @

"""


@format_to_csv
def return_sample():
    return [
        {"id": "1", "name": "lemon"},
        {"id": "2", "name": "orange"},
        {"id": "3", "name": "pineapple"}
    ]

print(return_sample())