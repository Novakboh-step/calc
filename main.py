from Numbers import Numbers
from Operations import Operations
from Validator import Validator

nums = Validator().check(input("Enter number 1: "), input("Enter number 2: "))
if nums != None:
    print(f"Result: {Operations().add(nums)}")
else:
    print("Wrong input")