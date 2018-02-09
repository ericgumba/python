def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """ 


    """
    Idea: 
    Count the number of zeroes there are in the array.

    Subtract the amount of zeros with length of array.

    Call that variable n.

    Now we move n objects.

    
    
    the first non zero we encounter we move that to 
    first position in array. Decrease n by 1

    Next non-zero we 

    """ 
    i = 0
    for index, num in enumerate(nums): 
        if num != 0:
            nums[i], nums[index] = nums[index], nums[i]
            i += 1
        
    print(nums)

moveZeroes(1)