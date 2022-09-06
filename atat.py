### Author: Adam Fehse
### Course: CSc 110
### Description: Make an AT-AT that can accept three inputs
###              and adjust three different sections of the machine.


neck = int(input('Neck Length:\n'))
body = int(input('Body Height:\n'))
leg = int(input('Leg Height:\n'))

print('')

### Passing white space to the end='' tells python no newline
print('     _..-Y  |  |  Y-._')
print(' .--"   ||  |  |  |   "-.')
print(' |______________________|\n' * body, end='')
print(' |______________________|', ' ' * neck + '   _____')
print(' L______________________[' + '-' * neck + '----------).')
print('I____________________ [__L]' + '_' * neck + '[----(_}--P')
print('L________________________j~', ' ' * neck + '\'+++++++//')
print('\\________________________]')
print('  [___________________]')
print('     I--I"~~"""~~"I--I')
print('     |\\n|         |\\n|\n' * leg, end="")
print('     ([])         ([])')
print('    /||||\\       /||||\\')
print('   |=}--{=|     |=}--{=|')
print('  .-4----4-.   .-4----4-.')
