# print('hello')
# print('hi, how are you doing?')
# print('hello world')
# name = input('what\'s yor name? ')
# print(name + ' loves blue color')
# dob = input('date of birth')
# dob = int(dob)
# print(type(dob))

# x= 1
# print(f"Wow, the value of x is {x}")

# x=5
# y=2
# if x> 1 or y<2:
#     print("This is true")
# else:
#     print("this is false")

# items = [10, 20, 30]
# sum =0
# for item in items:
#     sum += item
# print(sum)

items = [10, 20, 30, 20, 10]
# for number in items:
    # i=0
    # while i<number:
    #     print("*", end=" ")
    #     i+=1
    # print('',end='\n')

# for i in items:
#     x = items.count(i)
#     if x > 1:
#         items.remove(i)
# print(items)
#
# message = input(">")
# words = message.split(" ")
# emojis ={
#     ":)": "😃",
#     ":(": "😧",
#     "XD": "😆",
# }
# output = " "
# for word in words:
#     output += emojis.get(word, "(replacement if key not in dict.)") + " " # This method tells the value corresponding to the key, (
# print(output)

def greet_user(firstName, lasName):
    print(f"Hello There {firstName} {lasName}!")
    print("Please have a seat")

print("START")
greet_user("JOHN", lasName="Smith") # First positional then named arguments.
print("STOP")




