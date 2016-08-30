import random
import time

# Bubble Sort #
def bubble_sort(my_list):
    for i in range(len(my_list),-1,-1):
        for j in range(i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

# less optimised bubble sort which searches through the entire list each iteration
def __bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)-1):
            if (my_list[j]) > (my_list[j+1]):
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
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

# Quick Sort #
def quick_sort(my_list):
    if len(my_list) < 2: return my_list
    # randomly select pivot
    pivot = random.randint(0,len(my_list)-1)
    index = 0
    while index < pivot:
        if my_list[index] > my_list[pivot]:
            my_list[index], my_list[pivot-1] = my_list[pivot-1], my_list[index]
            my_list[pivot-1], my_list[pivot] = my_list[pivot], my_list[pivot-1]
            pivot -= 1
        else:
            index += 1
    in_place = [my_list[pivot]]
    left = my_list[:pivot]
    right = my_list[pivot+1:]
    return quick_sort(left) + in_place + quick_sort(right)


# ---------------------------------

# Heap Sort #
def heap_sort(my_list):
    if len(my_list) < 2: return my_list
    length = len(my_list)
    my_list = heapify(my_list)
    print "heapified", my_list
    while length > 2:
        print "length", length
        my_list[0], my_list[length-1] = my_list[length-1], my_list[0]
        length = length - 1
        parent = 0
        left = 1
        if length > 2:
            right = 2
        else:
            right = None
        print "parent", my_list[parent]
        print "left", my_list[left]
        if right != None:
            print "right", my_list[right]
        print my_list
        my_list = sift_down(my_list[:length], parent, left, right) + my_list[length:]
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
        """
        print "parent", my_list[parent_index]
        print "left", my_list[left_child_index]
        if right_child_index != None:
            print "right", my_list[right_child_index]
        print my_list
        """
        my_list = sift_down(my_list, parent_index, left_child_index, right_child_index)
        parent_index -= 1
        left_child_index -= 2
        right_child_index = left_child_index +1


    return my_list

def sift_down(my_list, parent, left, right):
    if right != None:
        if my_list[parent] > my_list[left] and my_list[parent] > my_list[right]:
            return my_list
        elif my_list[left] > my_list[right]:
            my_list[parent], my_list[left] = my_list[left], my_list[parent]
            parent = left
            left = ((parent + 1) * 2) - 1
            right = ((parent + 1) * 2)
            if right > len(my_list) - 1:
                right = None
            if left < len(my_list) and right < len(my_list):
                sift_down(my_list, parent, left, right)
            return my_list
        else:
            my_list[parent], my_list[right] = my_list[right], my_list[parent]
            parent = right
            left = ((parent + 1) * 2) - 1
            right = ((parent + 1) * 2)
            if right > len(my_list) - 1:
                right = None
            if left < len(my_list) and right < len(my_list):
                sift_down(my_list, parent, left, right)
            return my_list
    else:
        if my_list[parent] > my_list[left]:
            return my_list
        else:
            my_list[parent], my_list[left] = my_list[left], my_list[parent]
            return my_list



# Testing #

my_nums = [1,99,7,64,-21,400,0,169,17,1,100,999]

my_randoms = random.sample(range(99), 8)
print heap_sort(my_nums)
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
    sort_my_randoms = merge_sort(my_randoms)
elif type_sort == 4:
    type_sort = "quick sort"
    sort_my_randoms = quick_sort(my_randoms)
elif type_sort == 5:
    type_sort = "heap sort"
    sort_my_randoms = heap_sort(my_randoms)
else:
    type_sort = "python sort"
    sort_my_randoms = sorted(my_randoms)

function_time = time.time() - start_time
print sort_my_randoms, "\ntype: %s, time: %s seconds" % (type_sort, function_time)
