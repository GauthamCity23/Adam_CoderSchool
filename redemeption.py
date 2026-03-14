user = int(input("Please enter a number: "))
quarter = 25
nickel = 5
dime = 10
penny = 1
total = 0
qused = 0
nused = 0
dused = 0
pused = 0
if user > 100:
    user = int(input("Please enter a number: "))

elif user < 1:
    user = int(input("Please enter a number: "))

qused = user // quarter
print(qused)
total += qused
user = user - (quarter*qused)
dused = user // dime
print(dused)
total += dused
user = user - (dime*dused)
nused = user // nickel
print(nused)
total += nused
user = user - (nickel*nused)
pused = user // penny
print(pused)
total += pused
user = user - (penny*pused)

if total <= 6:
    print(total)
else:
    print('Too many coins')
