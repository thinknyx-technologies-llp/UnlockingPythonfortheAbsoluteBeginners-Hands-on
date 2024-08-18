a = 5
b = 0
try:
    x = a/b
except:
    print("Value of b is 0")
finally:
    print("This block of code will always execute")