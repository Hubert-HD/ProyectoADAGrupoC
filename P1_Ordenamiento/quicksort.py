from insertionsort import insertionSort

def partition(arr, left, right):
	pivot = arr[right]
	i = j = left
	for i in range(left, right):
		if arr[i] < pivot:
			arr[i], arr[j] = arr[j], arr[i]
			j += 1
	arr[j], arr[right] = arr[right], arr[j]
	return j

def quickSortOptimized(arr, left, right):
	umbral = 10
	while left < right:
		if right - left + 1 < umbral:
			subarr = arr[left : right + 1]
			insertionSort(subarr)
			arr[left : right + 1] = subarr
			break
		else:
			pivot = partition(arr, left, right)
			if pivot - left < right - pivot:
				quickSortOptimized(arr, left, pivot - 1)
				left = pivot + 1
			else:
				quickSortOptimized(arr, pivot + 1, right)
				right = pivot - 1

def quickSort(arr):
	quickSortOptimized(arr, 0, len(arr) - 1)