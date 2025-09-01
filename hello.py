# Ask Name
# \' makes ' literal
cmd = input('What\'s your name? ')

# Remove space from string
cmd = cmd.strip()

''' Capitalize the user's name 
    cmd = cmd.capitalize() only capitalizes first letter of the string not every word 
'''
# cmd = cmd.title() makes the string into title format [i.e, capitalizes every word]
cmd = cmd.title()
name = cmd

#Split the name into two variables
first, last = cmd.split(' ')

# Say Hello to user
# sep & end are parameters of " printf()" fn
print('Hello',first, sep='_', end=' :) \n')
print('I know your full name is ', name)
