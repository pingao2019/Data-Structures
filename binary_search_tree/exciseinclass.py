# classroom excise for recursion 
# To find the target value in an array:

def recur_search(unsorted_array, target):
    if len(unsorted_array)== 0:
        return False
    if unsorted_array[-1] == target:
        return True
    return recur_search (unsorted_array[:-1], target)
ua =[23,3,4,8,12,22]
print(recur_search(ua, 22))