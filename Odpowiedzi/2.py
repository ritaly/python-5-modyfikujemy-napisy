# -*- coding: utf8 -*-

"""
Pobierz od użytkownika imię, nazwisko i numer telefonu,
a następnie:
    * Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
    * Imię nazwisko popraw na pisane z dużej litery
    * Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
    * Sprawdź czy użytkownik jest kobietą
    * Połącz dane w jeden ciąg za pomocą spacji
    * Policz liczbę wszystkich znaków ww napisie
    * Podaj liczbę tylko liter w napisie
"""

name = input("Imię: ")
surname = input("Nazwisko: ")
number = input("Numer telefonu: ")

print("Czy imię składa się tylko z liter?", name.isalnum())
print("Czy nazwisko składa się tylko z liter?", surname.isalnum())
print("Czy numer telefonu składa się z cyfr", number.isdigit())

print(name, surname)
name = name.capitalize()
surname = surname.capitalize()
print(name, surname)

print(number)
number = number.replace(" ", "").replace("-","")
print(number)

print("Imię kobiece:", name.endswith("a"))

personal = name + " " + surname + " " + number
print(personal)
print(len(personal))

letters = len(personal) - personal.count(" ") - 9
print(letters)
print (len(name + surname)) #sprawdzenie

