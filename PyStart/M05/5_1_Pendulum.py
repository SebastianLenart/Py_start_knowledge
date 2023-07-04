import pendulum # czemu tu nie czyta ale z cmd dziala

dt = pendulum.now()
print(dt.format("dddd DD MMMMM YYYY", locale="pl"))

"""
pip freeze ? requirements.txt
pip install -r requirements.txt

"""

"""
zarzadzanie wirtualnym srodowiskiem

poetry

pipenv


"""