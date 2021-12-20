def selectionSort(array):
    """Complexity : O(n**2)"""
    for i in range(len(array)-1):
        indexMinValue = array[i:].index(min(array[i:])) + i
        array[i], array[indexMinValue] = array[indexMinValue], array[i]
    return array

def selectionSortRecursive(array, index=0):
    """Complexity : O(n**2)"""
    if len(array) - 1 > index:
        indexMinValue = array[index:].index(min(array[index:])) + index
        array[index], array[indexMinValue] = array[indexMinValue], array[index]
        selectionSortRecursive(array, index + 1)
    return array