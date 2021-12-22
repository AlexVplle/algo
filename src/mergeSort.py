def mergeSort(array):
    """Complexity : O(nlog(n))"""
    lengthArray = len(array)
    if lengthArray > 1:
        arrayMiddle = lengthArray // 2
        leftArray, rightArray = array[:arrayMiddle], array[arrayMiddle:]
        array.clear()
        mergeSort(leftArray)
        mergeSort(rightArray)
        while leftArray and rightArray:
            array.append(leftArray.pop(0) if leftArray[0] < rightArray[0] else rightArray.pop(0))
        array.extend(leftArray)
        array.extend(rightArray)
    return array            