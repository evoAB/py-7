b=int(input("Enter year : "))
print("a.Non century leap year")
print("b. Century leap year")
print("c. Non century non leap year")
print("d. Century non leap year") 
match input("Enter your choice "):
    case 'a':
        match b%100==0 and b%400!=0:
            case 1:
                print("Not a Non century leap year")
            case 0:
                print("Non century leap year")
    
    case 'b':
        match b%100==0 and b%400!=0:
            case 1:
                print("Century leap year")
            case 0:
                print("Not a century leap year")

    case 'c':
        match b%100!=0 and b%4!=0:
            case 1:
                print("Non century non leap year")
            case 0:
                print("Not a Non century non leap year")
    
    case 'd':
        match b%100==0 and b%4!=0:
            case '1':
                print("Century non leap year")
            case '0':
                print("Not a Century non leap year")

    case _:
        print("Invalid input")