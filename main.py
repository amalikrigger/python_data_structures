def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [2, 3, 4, 10, 40]

x = 10

result = linear_search(arr, x)

print(result)

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

x = 40

result = binary_search(arr, x)

print(result)

def is_palindrome(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

name = 'azyza'
next_name = 'racecar'
other_name = 'car'

result = is_palindrome(name)

print(result)

result = is_palindrome(next_name)

print(result)

result = is_palindrome(other_name)

print(result)

def rotate_array(array, pos):
    length = len(array)
    k = pos % length
    reverse(array, 0, length - 1)
    reverse(array, 0, k - 1)
    reverse(array, k, length - 1)
    print(array)

def reverse(array, start, end):
    while start < end:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5]

rotate_array(arr, 10)



def longest_substring_without_repeating_characters(str):
    left = 0
    right = 0
    mx = 0
    length = len(str)
    seen = []

    while right < length:
        if str[right] not in seen:
            seen.append(str[right])
            right += 1
        else:
            while str[right] in seen:
                del seen[0]
                left += 1
        mx = max(mx, right - left)
    print(mx)

longest_substring_without_repeating_characters('pwwkew')


























