while True:
    ch = input("Want to enter a list?(y/n): ")

    if (ch == "y") or (ch == "Y"):
        ip = input("Enter a list elements separated by a comma: ")

        ip2 = ip.split(",")
        print("Input: list1 =  ", ip2)

        int_list=[int(x) for x in ip2]

        ip3 = list(filter(lambda y: y > 0, int_list))
        print("Output: ",ip3)

    elif (ch == "n") or (ch == "N"):
        break

    else:
        print("Please check your response!")