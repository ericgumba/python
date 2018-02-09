def rob(nums):

    table = []
    if len(nums) == 0:
        return 0
    # 4 2 2 4
    # 4 4 6 8
    # nums[i-2] + value or nums[i-1]

    for i, value in enumerate(nums):
        if i == 0:
            table.append(value)
        elif i == 1:
            if value > nums[i-1]:
                table.append(value)
            else:
                table.append(nums[i-1])
        else:
            print(nums[i-1], table[i-2] + value)
            if table[i-1] > table[i-2] + value:
                table.append(table[i-1])
            else: 
                table.append(table[i-2] + value)
     

    return table[-1]

print(rob([4,2,2,4]))


