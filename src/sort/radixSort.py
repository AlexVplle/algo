def radixSort(array : list) :
    """Complexity : O(n * number of max number's digits) for positive integers in array"""
    maxArray, exp = max(array), 1
    while maxArray // exp :
        array = countingSort(array, exp)
        exp *= 10
    return array
def countingSort(array : list, exp : int) :
    lengthArray = len(array)
    outputArray, countArray = [0] * lengthArray, [0] * 10
    for i in range(lengthArray) :
        countArray[array[i] // exp % 10] += 1
    for i in range(1, 10) :
        countArray[i] += countArray[i - 1]
    for i in range(lengthArray - 1, -1, -1) :
        index = array[i] // exp % 10
        countArray[index] -= 1
        outputArray[countArray[index]] = array[i]
    return outputArray
