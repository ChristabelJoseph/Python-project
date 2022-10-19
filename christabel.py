'''
year = (input("type year of birth: "))
Age = 2022 - int(year)
if Age > 18:
    print("you are qualified")
else:
    print("Too young")
print(Age)

'''
'''
year = (input("type year of birth: "))
Age = 2022 - int(year)
if Age  > 60:
    print("too old")
elif Age <= 30:
    print("you are qualified")
else: 
    print("not qualified")
'''
'''
Username = input("username: ")

if Username =="": 
    print("you did not enter a username")
Pin = input("Pin: ")  
if len(Pin) != 4:
    print ("Pin must be 4 digits")
'''
'''
from ctypes.wintypes import PUINT


username = input("username: ")
pin = input("pin: ")
if username =="" or len(pin) != 4:
    print ("you have a big problem")
'''

from calendar import c
from re import A


score = int(input("score: "))
if score >= 80:
    print ("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
elif score >= 40:
    print("D")
elif score >= 20:
    print("E")
else:
   print("F")