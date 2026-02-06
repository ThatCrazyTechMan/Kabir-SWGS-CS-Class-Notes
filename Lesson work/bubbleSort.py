items = ["a", "c", "d", "b", "e"]
n = len(items) -1
swapped = True
while n > 0 and swapped == True:
    swapped = False
    for i in range(0,n):
        if items[i] > items[i+1]:
            items[i], items[i+1] = items[i+1], items[i]

