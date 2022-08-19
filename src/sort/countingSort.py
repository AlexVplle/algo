def countingSort(array : list):
    """Complexity : O(n + k) for posiive integers in array"""
    output = [0 for _ in range(max(array) + 1)]
    for i in array:
        output[i] += 1
    ind = 0
    for i in range(len(output)):
        for _ in range(output[i]):
            array[ind] = i
            ind += 1
    return array
