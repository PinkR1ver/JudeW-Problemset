from random import randint

def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

x = input()
n = int(x.split(' ')[0])
q = int(x.split(' ')[1])

growth = input().split(' ')
growth = [int(n) for n in growth]

output = []

for i in range(q):
    cast = input().split(' ')
    cast = [int(n) for n in cast]
    difference = n
    seq = growth[cast[0] - 1:cast[1]]
    seq = quicksort(seq)
    for index, elem in enumerate(seq):
        if index + 1 < len(seq):
            if abs(elem - seq[index + 1]) < difference:
                difference = abs(elem - seq[index + 1]) 
    output.append(difference)

for i in output:
    print(i)