s1 = input("Enter first sting ")
s2 = input("Enter second string ")
match (s1,s2):
    case (s1,s2) if s1==s2:
        print("Identical Strings")
    case (s1,s2) if s1>s2:
        print("{} come after {}".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} come after {}".format(s2,s1))