
width = int(input('Enter number:\n'))

# its 9 spaces wide for empty strings due to
# the cockpit is 9 spaces wide at the smallest.
print('|[' + ' ' * width + '         ' + ' ' * width + ']|')
print('|[' + ' ' * width + ' /=---=\\ ' + ' ' * width + ']|')
print('|[' + '/' * width + '|== X ==|' + '\\' * width + ']|')
print('|[' + ' ' * width + ' \\=---=/ ' + ' ' * width + ']|')
print('|[' + ' ' * width + '         ' + ' ' * width + ']|')

