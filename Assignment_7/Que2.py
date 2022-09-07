a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
match input("Enter operation : "):
    case '+':
        print("Sum =",a+b)
    case '-':
        print("Substraction =",abs(a-b))
    case '*':
        print("Multiplication =",a*b)
    case '/':
        print("Division =",a/b)
    case _:
        print("Invalid Operation")
