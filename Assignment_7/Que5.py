a=int(input("Enter a number : "))
match a:
    case a if a%2==0:
        print("Saurabh Shukla")
    case a if a%2==1 and a<0:
        print("Prateek Jain")
    case a if a%2==1 and a>0:
        print("Aditya Choudhary")