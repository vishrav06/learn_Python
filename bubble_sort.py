lis = [112,45,675,35,635,4,6]

def bubble_sort(lis):
    n = len(lis)
    for j in range(n):

        for i in range(n-j-1):
            if lis[i+1]<lis[i]:
                lis[i+1], lis[i] = lis[i], lis[i+1]

bubble_sort(lis) #passing list by reference
print(lis)