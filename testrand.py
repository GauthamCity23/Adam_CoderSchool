import random 
a = random.randint(1,100)
adam = int(input("Please enter a random number: "))
while adam < 1 or adam > 100:
    adam = int(input("Invalid Input, please enter a random number: "))

aiden = int(input("Please enter a random number: "))
while aiden < 1 or aiden > 100:
    aiden = int(input("Invalid Input, please enter a random number: "))

adam1 = int(input("Please enter a second random number: "))
while adam1 < 1 or adam1 > 100:
    adam1 = int(input("Invalid Input, please enter a second random number: "))

aiden1 = int(input("Please enter a second random number: "))
while aiden1 < 1 or aiden1 > 100:
    aiden1 = int(input("Invalid Input, please enter a second random number: "))

adam2 = int(input("Please enter a third random number: "))
while adam2 < 1 or adam2 > 100:
    adam2 = int(input("Invalid Input, please enter a third random number: "))

aiden2 = int(input("Please enter a third random number: "))
while aiden2 < 1 or aiden2 > 100:
    aiden2 = int(input("Invalid Input, please enter a third random number: "))

adam_sum = abs(adam+adam1+adam2 / 3.0)
aiden_sum = abs(aiden+aiden1+aiden2 / 3.0)

if abs(adam_sum - a) > abs(aiden_sum - a):
    print('Player 1 wins')

elif abs(adam_sum - a) < abs(aiden_sum - a):
    print("Player 2 wins")

else:
    print("Tie")

print('Computer guess was ',a)
