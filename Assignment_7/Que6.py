a = input("Enter a string : ")

match a:
    case a if ' ' in a:
        print("Multiword String")
    case a if ' ' not in a:
        print("Single word String")