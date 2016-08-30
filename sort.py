import random
import time

#1. Bubble Sort, least efficient
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

# ---------------------------------

#2. Insertion Sort
def insertion_sort(my_list):
    if len(my_list) < 2: return my_list
    sorted = 1
    for i in range(1,len(my_list)):
        index = 0
        while index < sorted and my_list[i] > my_list[index]:
            index += 1
        item = my_list.pop(i)
        my_list.insert(index, item)
        sorted += 1
    return my_list

# ---------------------------------

#3. Merge Sort
def merge_sort(my_list):
    if (len(my_list) < 2):
        return my_list
    middle = len(my_list)/2
    left = my_list[:middle]
    right = my_list[middle:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    left_len = len(left)
    right_len = len(right)
    merge_len = left_len + right_len
    merge = [0] * merge_len

    left_index = 0
    right_index = 0
    merge_index = 0

    # merge
    while left_index < left_len and right_index < right_len:
        if left[left_index] <= right[right_index]:
            merge[merge_index] = left[left_index]
            left_index += 1
        elif right_index < right_len:
            merge[merge_index] = right[right_index]
            right_index += 1
        merge_index += 1

    # add any leftover values in left
    while left_index < left_len:
        merge[merge_index] = left[left_index]
        left_index += 1
        merge_index += 1

    # add any leftover values in right
    while right_index < right_len:
        merge[merge_index] = right[right_index]
        right_index += 1
        merge_index += 1

    return merge

# ---------------------------------

start_time = time.time()
my_randoms = random.sample(range(999999),10000)
type_sort = input("Which type of sort? 1 = bubble, 2 = insertion, 3 = merge\n")
if type_sort == 1:
    type_sort = "bubble sort"
    sort_my_randoms = bubble_sort(my_randoms)
elif type_sort == 2:
    type_sort = "insertion sort"
    sort_my_randoms = insertion_sort(my_randoms)
elif type_sort == 3:
    type_sort = "merge sort"
    sort_my_randoms = merge_sort(my_randoms)
else:
    type_sort = "bubble sort"
    sort_my_randoms = bubble_sort(my_randoms)

function_time = time.time() - start_time
print sort_my_randoms, "\ntype: %s, time: %s seconds" % (type_sort, function_time)
