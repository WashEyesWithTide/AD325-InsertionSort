def insertion_sort(arr: list[int]) -> list[int]:
    """
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    print("Hello World")
    print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))