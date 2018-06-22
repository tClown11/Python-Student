def quick_sort(lists, left, right):
    #
    if left >= right:
        return lists
    #
    low = left
    high = right

    #
    key = lists[low]
    while low < high:
        #
        while low <