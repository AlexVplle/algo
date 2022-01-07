def countingSort(array):
    """Complexity : O(n + k) for posiive numbers in array"""
    output = [0 for i in range(max(array) + 1)]
    for i in array:
        output[i] += 1
    ind = 0
    for i in range(len(output)):
        for j in range(output[i]):
            array[ind] = i
            ind += 1
    return array



    