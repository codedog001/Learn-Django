import random

rint = random.randint(10, 20)
print(rint)

# Print random number 3 times: --------------------------------------------
for i in range(3):
    print(random.randint(1,10))

# ----------------------------------------------------------------------------------------
# Picking random from list
lister = ['mohit', 'monish', 'ashish', 'dheeraj']
niceGuy = random.choice(lister)
print(niceGuy)