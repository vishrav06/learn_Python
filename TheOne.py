# with open("practice.txt", "r") as f:
#     data = f.read()
#     new_date = data.replace("is", "are")

# print(new_date)

# with open("practice.txt", "w") as f:
#     f.write(new_date)


# with open("practice.txt", "r") as f:
#     data = f.read()
#     k = data.find("LP")

# print(k)


def find_line():
    line = 1
    with open("practice.txt", "r") as f:
        data = True
        while data:
            data = f.readline()
            if "LP" in data:
                print("Word at line ", line)
                return
            else:
                line+=1
    
    return -1


find_line()
