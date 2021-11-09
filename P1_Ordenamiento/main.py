from util import arrayGenerator
from heapsort import heapSort
from quicksort import quickSort

def validateSortInteger():
	arr1 = arrayGenerator(type="int", maxSize=15)
	arr2 = arr1.copy()
	print("lista 1: ", arr1)
	print("lista 2: ", arr2)
	heapSort(arr1)
	quickSort(arr2)
	print("lista 1 ordenada:",arr1)
	print("lista 2 ordenada:",arr2)
	if(arr1 == arr2):
		print("El ordenamiento de heapSort y quickSort en números enteros es el mismo")

def validateSortFloat():
	arr1 = arrayGenerator(type="float", maxSize=15)
	arr2 = arr1.copy()
	print("lista 1: ", arr1)
	print("lista 2: ", arr2)
	heapSort(arr1)
	quickSort(arr2)
	print("lista 1 ordenada:",arr1)
	print("lista 2 ordenada:",arr2)
	if(arr1 == arr2):
		print("El ordenamiento de heapSort y quickSort en números reales es el mismo")

def validateSortString():
	arr1 = arrayGenerator(type="string", maxSize=15)
	arr2 = arr1.copy()
	print("lista 1: ", arr1)
	print("lista 2: ", arr2)
	heapSort(arr1)
	quickSort(arr2)
	print("lista 1 ordenada:",arr1)
	print("lista 2 ordenada:",arr2)
	if(arr1 == arr2):
		print("El ordenamiento de heapSort y quickSort en cadenas de caracteres es el mismo")

def main():
	print("------Comparación de ordenamiento------\n")
	print("Comparación de ordenamiento en números enteros")
	validateSortInteger()
	print("------------")
	print("Comparación de ordenamiento en números reales")
	validateSortFloat()
	print("------------")
	print("Comparación de ordenamiento en cadenas de caracteres")
	validateSortString()
main()