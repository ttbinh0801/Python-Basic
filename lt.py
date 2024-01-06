# bt
# Input: [2, 1, 5, 3, 7, 9]
# Output: [1, 2, 3, 5, 7, 9]
# def sort_array(array):
#     pass
def sort_array(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j] > array[j+1]:
                temp= array[j]
                array[j]= array[j+1]
                array[j+1]= temp
    return array
print(sort_array([1,5,4,6,8,2,9]))