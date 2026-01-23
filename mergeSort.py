items = ["a", "c", "d", "b", "e", "g", "h", "t", "q", "l"]

def mergeSort(items):
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
    else:
        return items
    return merge(left, right)

def merge(left, right):
    newlist = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            newlist.append(left[0])
            left.pop(0)
        elif right[0] < left[0]:
            newlist.append(right[0])
            right.pop(0)
        else:
            newlist.append(left[0])
            newlist.append(right[0])
    while len(left) > 0:
        newlist.append(left[0])
        left.pop(0)
    while len(right) > 0:
        newlist.append(right[0])
        right.pop(0)
        




    return newlist

print(mergeSort(items))