### Author: Adam Fehse
### Course: CSc 110
### Description: Create a TIE fighter that can receive input
###              from the user and adjust in width.


### \n causes output to be advanced to the next line.
width = int(input('Enter TIE width:\n'))
print("")


### Had to use an extra \ because it acts as escape char.
print('|[' + ' ' * width + '         ' + ' ' * width + ']|')
print('|[' + ' ' * width + ' /=---=\\ ' + ' ' * width + ']|')
print('|[' + '/' * width + '|== X ==|' + '\\' * width + ']|')
print('|[' + ' ' * width + ' \\=---=/ ' + ' ' * width + ']|')
print('|[' + ' ' * width + '         ' + ' ' * width + ']|')
