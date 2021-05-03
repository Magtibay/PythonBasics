def basic_calculator():
    num1 = float(input("Enter a number: "))
    operator = input("Enter one of the following operations you wish to use ('+' , '-', '*', '/'): ")
    num2 = float(input("Enter another number: "))

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        print("Error: User did not select one of the options.")

print(basic_calculator())


