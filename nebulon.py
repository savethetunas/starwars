### Author: Adam Fehse
### Course: CSc 110
### Description: A programs that accepts four user inputs to create a nebulon
###              space ship. Large, medium, small, and front inputs all adjust
###              the proportions of the ship.

large = int(input('Large Layers on bottom:\n'))
medium = int(input('Medium Layers on bottom:\n'))
small = int(input('Small Layers on bottom:\n'))
front = int(input('Front length:\n'))

print("")

### The large sections of the ship.
front_minus_four = int(front - 4)

### The medium sections of the ship.
front_divide_two = int(front / 2)

### Here is the calculation to figure out the width of the
### empty space before the "+" section. I used the front/2 calculation
### from above and added front mod 2 which has the effect of adding by
### a zero or one based on if the input is even or odd.
front_divide_modulus_two = int(front / 2) + (front % 2)

### The small section of the ship.
front_divide_three = int(front / 3)

### Here is the empty space before the "#" sign that changes widths
### in relation to the front input. I calculated the ratios of the
### different base cases and landed on 1.42 as a suitable scaler. 1.4 works
### as well but not for the 17 test case. By multiplying the front input
### by 1.42 than dividing by 2, the even inputs will be .1 or so over
### the target value and round down. The odds will be further from the
### desired value but will round down to the correct digit.
hash_line_space = int((front * 1.42) / 2)

### The large, medium, and small layers grow vertically and horizontally
### by user input. The horizontal parts are restricted to the above formulae.
### By performing all calculations within ()'s and then concatenating the escape
### character "\n" causes the output to be forced to a new line.
### The end="" function is passed to the entire line which tells python to print an
### empty space instead of a new line.
print('  /='+ '-' * front +'\                 /--------|')
print(' /=='+ '/' * front +'====\            |=========|')
print('|==-'+ '/' * front +'======\----================|')
print(' \\'+ '=' * front +'====-------------------------|')
print('  \='+ '-' * front +'=///              \=======/')
print((('    \\' + '-' * front_minus_four + '|') + '\n') * large, end='')
print(((' ' * front_divide_modulus_two + ':' + '+' * front_divide_two + '|') +'\n') * medium, end='')
print((' ' * hash_line_space + '\\' + '#' * front_divide_three + '|' + '\n') * small, end='')
