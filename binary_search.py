#Binary Seach    
def binary_seach(array:int, target:int) -> bool:
    low=0
    high=len(array)-1
    mid=None
    
    while (high>=low):
        mid= int((low+high)/2)    # [1, 2] 3
        if (target==array[mid]):  #  0  1
            return True
        if (target>array[mid]):
            low=mid+1
        else:
            high=mid-1
            
    return False


numbers= [i for i in range(11)]
print(numbers, binary_seach(numbers, 0))
