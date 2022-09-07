a=int(input("enter first side : "))
b=int(input("enter second side : "))
c=int(input("enter third side : "))
print("a. isosceles triangle")
print("b. right angled triangle")
print("c. equilateral triangle")
print("d. exit")
match (input("Enter your choice : ")):
    case 'a':
        if(a==b or b==c or c==a):
            print("It is Isosceles Triangle")
        else:
            print("Not a Isosceles Triangle")
    case 'b':
        if(a**2+b**2==c or b**2+c**2==a**2 or c**2+a**2==b**2):
            print("It is right angled triangle")
        else:
            print("not a right angled triangle")
    case 'c':
        if(a==b==c):
            print("It is equilateral triangle")
        else:
            print("not a equilateral triangle")
    case 'd':
        pass
    case _:
        print("Invalid input")