def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(len(list)):
        if list[i]==target:
            return i
    return print('None')

list = [0,14,5,2,5,6,8,9,3]
linear_search(list,44)