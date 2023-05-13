# -*- coding utf-8 -*-

""" twos = [2 ** i for i in range(8)]
print(twos)

board = []

for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)

print(board) """

""" table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)' """
""" cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)' """
###

""" for i in range(1):
    print("#")
else:
    print("#") """

""" my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list) """
####
""" t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s) """
##
""" my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0]) """
##
""" def message():
    print("Ingresar valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input()) """