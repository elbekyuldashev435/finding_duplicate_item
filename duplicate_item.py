

def repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        k = i + 1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
item = repeat(array1)
if item is None:
    print("Duplicates not found")
else:
    print(f"Number ({item[0]}) is repeated in the {array1}")