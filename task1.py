def BinarySearch(list, find):
    first = 0
    last = len(list)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if list[mid] == find:
            index = mid
        else:
            if find<list[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(BinarySearch([1,2,3,3,4,5,6,6,7], 5))