lis = [12,45,675,35,635,4,6]

def selection_sort(lis):
    #selecting the position of array to be swapped
    for i in range(0,len(lis)-1): #1 less iteration since the last swap is not necessary
        min_index = i

        #finding the min number that has to go in the i'th position
        for j in range(i+1,len(lis)):
            if lis[j]<lis[min_index]:
                min_index = j
        
        lis[i], lis[min_index] = lis[min_index], lis[i] #swap

        

selection_sort(lis) #passing list by reference
print(lis)