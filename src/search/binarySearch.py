def binarySearch(array : list, target : int) :
    """Complexity : O(log(n))"""
    end = len(array) - 1
    mid = end // 2
    if not array : return 0
    valueMid = array[mid]
    if valueMid == target: return mid
    if len(array) == 1 : 
        if array[0] < target : return 1
        return 0
    if valueMid > target : return binarySearch(array[:mid], target)
    else : return mid + 1 + binarySearch(array[mid+1:], target)