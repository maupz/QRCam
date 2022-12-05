# -*- coding utf-8 -*-

winner_number = "24"

chosen_number = input("Hola Invitado, adivina que numero estoy pensando [Del 1 al 24]: ")

if winner_number == chosen_number:
    print("Haz adivinado, el número ganador es: " + winner_number)
else :
    print("No haz tenido suerte, el número ganador era: " + winner_number + ", pero elegiste el: " + chosen_number)