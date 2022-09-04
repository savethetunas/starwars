### Author: Adam Fehse
### Course: CSc 110
### Description: Create a TIE fighter that can receive input
###              from the user and adjust in width.


### \n causes output to be advanced to the next line.
### The int() function converts the value into an integer.
width = int(input('Enter number:\n'))
print("")


### I concatenated |[ to a space then multiplied that by the width variable.
### Then concatenated a string with 9 spaces + a single space.
### Then multiplied that by width plus ]|.
### Had to use an extra \ because it acts as escape char.
print('|[' + ' ' * width + '         ' + ' ' * width + ']|')
print('|[' + ' ' * width + ' /=---=\\ ' + ' ' * width + ']|')
print('|[' + '/' * width + '|== X ==|' + '\\' * width + ']|')
print('|[' + ' ' * width + ' \\=---=/ ' + ' ' * width + ']|')
print('|[' + ' ' * width + '         ' + ' ' * width + ']|')
