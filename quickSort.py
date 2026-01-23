items = ["a", "c", "d", "b", "e", "g", "h", "t", "q", "l"]
numbers = [4,1,7,9,3,6,2,1,3,5,0]

def quickSort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left_mark = 1
    right_mark = len(list) - 1
    while left_mark <= right_mark:
        while left_mark <= right_mark and list[left_mark] <= pivot:
            left_mark += 1
        while right_mark >= left_mark and list[right_mark] > pivot:
            right_mark -= 1
        if left_mark <= right_mark:
            list[left_mark], list[right_mark] = list[right_mark], list[left_mark]
        list[0], list[right_mark] = list[right_mark], list[0]

    return quickSort(list[:right_mark])+[list[right_mark]]+quickSort(list[right_mark+1:])




print(quickSort(numbers))
print(quickSort(items))