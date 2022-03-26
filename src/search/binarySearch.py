def binarySearchRecursive(array : list, target : int) :
    """Complexity : O(log(n))"""
    if target not in array : return -1
    end = len(array) - 1
    mid = end // 2
    valueMid = array[mid]
    if valueMid == target: return mid
    if valueMid > target : return self.search(array[:mid], target)
    else : return mid + 1 + self.search(array[mid+1:], target)

def binarySearchIterative(array : list, target : int) :
    """Complexity : O(log(n))"""
    start, end = 0, len(array) - 1
    while start <= end :
        mid = (start + end) // 2
        valueMid = array[mid]
        if valueMid == target : return mid
        if valueMid > target : end = mid - 1
        else : start = mid + 1
    return -1