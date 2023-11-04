# target=int(input("what your number"))

# for x in range(1,target+1):
#     if x%3==0 and x%5==0:
#         print("roger_andy")
#     elif x%3==0:
#         print("roger")
#     elif x%5==0:
#         print("andy")
#     else:
#         print(x)
    
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbol = "!@#$%^&*()"

user_lett = (input("你的字母: "))
user_numb = int(input("你的字母: "))
user_symb = str(input("你的字母: "))

password = ""

for x in range(user_lett):
    password += random.choice(letters)
for x in range(user_numb):
    password += random.choice(numbers)
for x in range(user_symb):
    password += random.choice(symbol)

password_list = list(password)
random.shuffle(password_list)
print(password_list)

password = ''.join(password_list)
print(password)
