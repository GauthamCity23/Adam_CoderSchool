total = int(input('Please enter a number between 50 and 150: '))
pennies = 1
dime = 10
nickel = 5
quarter = 25
pUse = 0
dUse = 0
nUse = 0
qUse = 0
leftover = 0
qUse = total // quarter
leftover = total - (quarter*qUse)
dUse = leftover // dime
leftover = leftover - (dime*dUse)
nUse = leftover // nickel
leftover = leftover - (nickel*nUse)
pUse = leftover
print('quarter:', qUse, 'dime:', dUse, 'nickel:', nUse, 'pennies:', pUse)
