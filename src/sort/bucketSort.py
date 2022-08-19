import functools

def bucketSort(array : list) :
    """Complexity : O(nlog(n))"""
    maxArray, lengthArray = max(array), len(array)
    bucket = [[] for _ in range(lengthArray)]
    for i in array :
        bucket[max(int((lengthArray - 1) * i // maxArray), 0)].append(i)
    for i in range(lengthArray) :
        bucket[i] = mergeSort(bucket[i])
    return functools.reduce(lambda a, b : a + b, bucket)

def mergeSort(array : list):
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
