large = int(input('Large Layers on bottom:\n'))
medium = int(input('Medium Layers on bottom:\n'))
small = int(input('Small Layers on bottom:\n'))
front = int(input('Front length:\n'))

front_minus_four = int(front - 4)

front_divide_two = int(front / 2)
front_divide_modulas_two = int(front / 2) + (front % 2)
front_modulas_two = int(front % 2)

front_divide_three = int(front / 3)


print('  /='+ '-' * front +'\                 /--------|')
print(' /=='+ '/' * front +'====\            |=========|')
print('|==-'+ '/' * front +'======\----================|')
print(' \\'+ '=' * front +'====-------------------------|')
print('  \='+ '-' * front +'=///              \=======/')
print((('    \\' + '-' * front_minus_four + '|') + '\n') * large, end='')
print(((' ' * front_divide_modulas_two + ':' + '+' * front_divide_two + '|') +'\n') * medium, end='')
print('       \\' + '#' * front_divide_three  + '|')



