import math

numbers = [1, 3, 5, 7, 9, 11, 13]


def binarySearch(array, start, end, element):
    if (end >= start)
            int mid = l + (r - l) / 2;

            // If the element is present at the middle itself
            if (arr[mid] == x)
                return mid;

            // If element is smaller than mid, then it can only
            // be present in left subarray
            if (arr[mid] > x)
                return binarySearch(arr, l, mid - 1, x);

            // Else the element can only be present in right
            // subarray
            return binarySearch(arr, mid + 1, r, x);
        } 
  
        // We reach here when element is not present in array 
        return -1; 


def searchElement(arr, element):
    return binarySearch(arr, 0, len(arr) - 1, element)


print(searchElement(numbers, 9))
