#--------M1 to find all numbers in a comma separated string-------
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""

#     for i in range(len(data)):
#         if data[i] == ",":
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]


#----------M2 to find all number in comma separated string--------

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    lis1 = data.split(",")
    print(lis1)

    for val in lis1:
        if int(val)%2==0:
            print("Even", end=", ")
        else:
            print("Odd", end=", ")

