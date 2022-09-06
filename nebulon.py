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
front_minus_four = int(front - 4)
front_divide_three = int(front / 3)
front_divide_two = int(front / 2)

### detects odd's then adds a one them
front_divide_modulus_two = int(front / 2) + (front % 2)

### 1.42 is a suitable scaler based on base case ratios.
hash_line_space = int((front * 1.42) / 2)

### Performing most calculations within ()'s then adding escapes
print('  /='+ '-' * front +'\                 /--------|')
print(' /=='+ '/' * front +'====\            |=========|')
print('|==-'+ '/' * front +'======\----================|')
print(' \\'+ '=' * front +'====-------------------------|')
print('  \='+ '-' * front +'=///              \=======/')
print((('    \\' + '-' * front_minus_four + '|') + '\n') * large, end='')
print(((' ' * front_divide_modulus_two + ':' + '+' * front_divide_two + '|') +'\n') * medium, end='')
print((' ' * hash_line_space + '\\' + '#' * front_divide_three + '|' + '\n') * small, end='')
