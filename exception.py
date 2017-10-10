import math

anumber = int(input("Please enter an integer "))

try:
   print(math.sqrt(anumber))
except:
   print("Bad Value for square root")
   print("Using absolute value instead")
   print(math.sqrt(abs(anumber)))