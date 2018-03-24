# -*- coding: utf8 -*-

"""
Do zmiennej zapisz zdanie: „Kurs Pythona jest prosty i przyjemny.”,
    * Policz znaki w napisie
    * Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
    * Wyświetl znak o indeksie:
        7
        12
        -4
        37
    * Wprowadź do zdania 2 błędy ortograficzne
"""

sentence = "Kurs Pythona jest prosty i przyjemny."

length = len(sentence)
print(length, "\n")


print(sentence)
print("znak o indeksie 7: ", sentence[7])
print("znak o indeksie 12:", sentence[12])
print("znak o indeksie 4 od końca:", sentence[-4])
print("znak o indeksie 37 nie istnieje. Zdanie ma 37 znaków numerowane od 0 - 36,\
      ostatni znak to kropka:", sentence[36], "\n")

sentence = sentence.replace("u","ó")
sentence = sentence.replace("rz", "ż")
print(sentence)
