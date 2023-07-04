def remove_vowels(text: str) -> str:
    vowels = "aeyouiąęAEYOUIAE"
    # result = ""
    # for char in str(text):
    #     if char not in vowels:
    #         result += char
    # return result
    return "".join(char for char in str(text) if char not in vowels)

def test_remove_vowels():
    assert  remove_vowels("Ala ma kota") == "l m kt"
    assert  remove_vowels("Wolę Pythona") == "Wl Pthn"
    assert  remove_vowels("123") == "123"
    assert  remove_vowels("") == ""

    

# python -m pytest 1_2_TDD_zad1.py -vvv

