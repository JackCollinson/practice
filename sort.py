import random

def bubble_sort(my_list):
    res = list(my_list)
    for i in range(len(res),-1,-1):
        for j in range(i-1):
            if (res[j]) > (res[j+1]):
                temp = res[j]
                res[j] = res[j+1]
                res[j+1] = temp
    return res

# less optimised bubble sort which searches through the entire list each iteration
def __bubble_sort(my_list):
    res = list(my_list)
    for i in range(len(res)):
        for j in range(len(res)-1):
            if (res[j]) > (res[j+1]):
                temp = res[j]
                res[j] = res[j+1]
                res[j+1] = temp
    return res

def insertion_sort(my_list):
    if len(my_list) < 2: return my_list
    sorted = 1
    for i in range(1,len(my_list)):
        index = 0
        while index < sorted and my_list[i] > my_list[index]:
            index += 1
        item = my_list[i]
        my_list.pop(i)
        my_list.insert(index, item)
        sorted += 1
    return my_list

def merge_sort(my_list):
    if (len(my_list) < 2):
        return my_list
    middle = len(my_list)/2
    left = my_list[:middle]
    right = my_list[middle:]
    return _merge(merge_sort(left), merge_sort(right))

def _merge(L, R):
    n1 = len(L)
    n2 = len(R)
    res = [0] * (n1 + n2)
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = 0     # Initial index of merged subarray


    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            res[k] = L[i]
            i += 1
        else:
            res[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        res[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        res[k] = R[j]
        j += 1
        k += 1

    return res


my_randoms = random.sample(range(999999),10000)
print insertion_sort(my_randoms)
