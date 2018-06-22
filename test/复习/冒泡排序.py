def bubble_sort(lists):
    #
    count = len(lists) - 1
    for index in range(count, 0, -1):
        #
        for sub_index in range(index):
            #
            if lists[sub_index] > lists[sub_index + 1]:
                lists[sub_index],lists[sub_index + 1] = lists[sub_index + 1], lists[sub_index]
    return lists

alist = [0,45,54,54,9,15]
print(bubble_sort(alist))