#Bubble Sort Implementation Practice

def bubble_sort(list_of_nums):
    unsorted_list = len(list_of_nums) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_list):
            if list_of_nums[i] > list_of_nums[i+1]:
                sorted = False
                list_of_nums[i], list_of_nums[i+1] = list_of_nums[i+1], list_of_nums[i]
        


list_of_nums = [70,45,98,1,2,6,4,100,3,20,40,5]

bubble_sort(list_of_nums)

print(list_of_nums)

