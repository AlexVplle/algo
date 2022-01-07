def heapSort(array):
    """Complexity : O(nlog(n))"""
    lengthArray = len(array)
    for i in range(lengthArray // 2 - 1, -1, -1):
        restoreHeap(array, lengthArray, i)
    for i in range(lengthArray - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        restoreHeap(array, i, 0)
    return array

def restoreHeap(array, lastIndex, evaluatedRoot):
    maxValue = evaluatedRoot
    left, right = 2 * evaluatedRoot + 1, 2 * evaluatedRoot + 2
    if left < lastIndex and array[maxValue] < array[left]:
        maxValue = left
    if right < lastIndex and array[maxValue] < array[right]:
        maxValue = right
    if maxValue != evaluatedRoot:
        array[evaluatedRoot], array[maxValue] = array[maxValue], array[evaluatedRoot]
        restoreHeap(array, lastIndex, maxValue) 
