def binary_search(list, target):
    """
    Return an index of the target position if not return None
    """
    first = 0
    last = len(list)-1
    while first<last:
        midpoint = (first + last) //2
        if list[midpoint] == target:
            return midpoint
        elif list[first] - target <1 or target - list[first]<1:
            return None
        elif list[midpoint]<target:
            first = midpoint
        elif list[midpoint]>target:
            last = midpoint
        
        print(first, '  ', last)
def verify(result):
    if result is not None:
        print("The index of the target is ", result)
    else:
        print("There is no result") 
list=range(50,101)
target = 50.5
result = binary_search(list,target)
verify(result)
            
        