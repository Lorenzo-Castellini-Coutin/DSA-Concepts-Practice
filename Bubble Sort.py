#Bubble Sort Algorithm Implementation Practice

def bubble_sort(list_of_nums):
    unsorted_list = len(list_of_nums) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_list):
            if list_of_nums[i] > list_of_nums[i+1]:
                sorted = False
                list_of_nums[i], list_of_nums[i+1] = list_of_nums[i+1], list_of_nums[i]
        




