import random
import time
import math
import sys

# Bubble Sort #
def bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list) - 1, i, -1):
            if my_list[j] < my_list[j-1]:
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
    return my_list

# ---------------------------------

# Insertion Sort #
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

# Merge Sort #
def merge(my_list, p, q, r):
    L = my_list[p:q+1]
    R = my_list[q+1:r+1]
    L.append(sys.maxint)
    R.append(sys.maxint)

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            my_list[k] = L[i]
            i += 1
        else:
            my_list[k] = R[j]
            j += 1
    return my_list

def merge_sort(my_list, p, r):
    if p < r:
        q = (p + r)/2
        merge_sort(my_list, p, q)
        merge_sort(my_list, q + 1, r)
        merge(my_list, p, q, r)
    return my_list

# ---------------------------------

# Quick Sort #
def quick_sort(my_list, p, r):
    if p < r:
        q = partition(my_list, p, r)
        quick_sort(my_list, p, q-1)
        quick_sort(my_list, q+1, r)
    return my_list

def partition(my_list, p, r):
    x = my_list[r]
    i = p - 1
    for j in range(p, r):
        if my_list[j] <= x:
            i += 1
            my_list[i], my_list[j] = my_list[j], my_list[i]
    my_list[i+1], my_list[r] = my_list[r], my_list[i+1]
    return i + 1

# ---------------------------------

# Heap Sort #
def heap_sort(my_list):
    if len(my_list) < 2:
        return my_list

    unsorted = len(my_list)

    # turn list into heap with heapify()
    my_list = heapify(my_list)

    # swap first and last elements of list
    my_list[0], my_list[unsorted-1] = my_list[unsorted-1], my_list[0]
    unsorted -= 1
    while unsorted > 1:


        parent = 0
        left = parent + 1
        if unsorted > 2:
            right = parent + 2
        else:
            right = None

        my_list = sift_down(my_list[:unsorted], parent, left, right) + my_list[unsorted:]
        my_list[0], my_list[unsorted-1] = my_list[unsorted-1], my_list[0]
        unsorted -=  1

    return my_list

def heapify(my_list):
    middle = len(my_list)/2

    parent_index = middle - 1

    left_child_index = (middle * 2) - 1

    if left_child_index + 1 < len(my_list):
        right_child_index = left_child_index + 1
    else:
        right_child_index = None

    while parent_index > -1:
        my_list = sift_down(my_list, parent_index, left_child_index, right_child_index)
        parent_index -= 1
        left_child_index -= 2
        right_child_index = left_child_index + 1


    return my_list

def sift_down(my_list, parent, left, right):

    if (my_list[left] > my_list[parent] and
            (right == None or my_list[left] > my_list[right])):

        my_list[parent], my_list[left] = my_list[left], my_list[parent]
        parent = left
        left = ((parent + 1) * 2) - 1
        right = left + 1

        if left < len(my_list) and right < len(my_list):
            sift_down(my_list, parent, left, right)

    elif right != None and my_list[right] > my_list[parent]:

        my_list[parent], my_list[right] = my_list[right], my_list[parent]
        parent = right
        left = ((parent + 1) * 2) - 1
        right = left + 1

        if left < len(my_list) and right < len(my_list):
            sift_down(my_list, parent, left, right)

    return my_list

# ---------------------------------

# Testing #
my_nums = [1,99,7,64,-21,400,0,169,17,1,100,999]
my_randoms = random.sample(range(99999), 10000)

type_sort = input("Which type of sort? "
                    "1 = bubble, "
                    "2 = insertion, "
                    "3 = merge, "
                    "4 = quick, "
                    "5 = heap, "
                    "default = python built-in\n")

start_time = time.time()

if type_sort == 1:
    type_sort = "bubble sort"
    sort_my_randoms = bubble_sort(my_randoms)
elif type_sort == 2:
    type_sort = "insertion sort"
    sort_my_randoms = insertion_sort(my_randoms)
elif type_sort == 3:
    type_sort = "merge sort"
    sort_my_randoms = merge_sort(my_randoms, 0, len(my_randoms)-1)
elif type_sort == 4:
    type_sort = "quick sort"
    sort_my_randoms = quick_sort(my_randoms, 0, len(my_randoms)-1)
elif type_sort == 5:
    type_sort = "heap sort"
    sort_my_randoms = heap_sort(my_randoms)
else:
    type_sort = "python sort"
    sort_my_randoms = sorted(my_randoms)

function_time = time.time() - start_time
print sort_my_randoms, "\ntype: %s, time: %s seconds" % (type_sort, function_time)
