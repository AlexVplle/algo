def bubbleSort(array):
    """Complexity : O(n**2)"""
    arrayLength = len(array)
    for i in range(arrayLength):
        swapped = False
        for j in range(arrayLength-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array
