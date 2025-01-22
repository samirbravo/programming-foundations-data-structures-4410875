def find_second_smallest(my_list):
    smallest = my_list[0]
    second_smallest = my_list[0]
    for i in my_list:
        if (i < smallest) :
            second_smallest = smallest
            smallest = i

        elif(i < second_smallest and i != smallest) :
            second_smallest = i
    return second_smallest

def find_second_smallest_v2(my_list):
    sorted_list = sorted(my_list)
    return sorted_list[1]

print(find_second_smallest_v2([5, 8, 3, 2, 6]))
