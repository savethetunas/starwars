
width = int(input('Enter TIE width:\n'))
print('')
# its 9 spaces wide foe empty strings due to
# the cockpit is 9 spaces wide at the smallest.
print('|[' + ' ' * width + '         ' + ' ' * width + ']|')
print('|[' + ' ' * width + ' /=---=\\ ' + ' ' * width + ']|')
print('|[' + '/' * width + '|== X ==|' + '\\' * width + ']|')
print('|[' + ' ' * width + ' \\=---=/ ' + ' ' * width + ']|')
print('|[' + ' ' * width + '         ' + ' ' * width + ']|')
