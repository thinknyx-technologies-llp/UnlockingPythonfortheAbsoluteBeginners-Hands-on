age = int(input("Enter your age: "))

if age < 18:
    print("You are not eligible to vote and not eligible for marriage")
else:
    print("You are eligible to vote.")
    if age >=21:
        print("You are also eligible for marriage.")
    else:
        print("You are not eligible for marriage yet.")