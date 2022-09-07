s=input("What is your favourite colour : ")
l1=["yellow","blue","orange","white","black","red"]
for colour in l1:
    if colour in s:
        c=colour
        break
    else:
        c="other"

match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")
