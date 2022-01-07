def quickSort(array, start=0, end=-1):
    """Complexity : O(n**2)"""
    if end == -1:
        end += len(array)
    if end > start:
        indexPivot = start
        for i in range(start, end):
            if array[i] <= array[end]:
                array[i], array[indexPivot] = array[indexPivot], array[i]
                indexPivot += 1
        array[indexPivot], array[end] = array[end], array[indexPivot]
        quickSort(array, start, indexPivot-1)
        quickSort(array, indexPivot+1, end)
    return array