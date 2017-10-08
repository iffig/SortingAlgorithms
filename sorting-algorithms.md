# Sorting Algorithms

* [Insertion Sort](#insertion-sort)
* [Mergesort](#mergesort)
* [Quicksort](#quicksort)


## Insertion Sort 

###### How It Works

In this sorting method, there are two sections of the array: sorted and unsorted. To start, the whole array is the unsorted portion, 
and the sorted portion is empty. Begin by looking at the first element. Since there is nothing to compare to, you can add it to the 
sorted portion of the array. Next you loop through the rest of the array, looking at each indivisual element. For each element, you 
will find its place in the sorted portion of the array by comparing with values to the left, until the whole array is sorted. 

###### Pseudocode 

```
  InsertionSort(array)
    For i = 1 to n
      element = array[i]
      j = i-1;
      while key < array[j] and 0 < j
        array[j+1] = array[j] 
        j -= j
     array[j+1] = 0
```

###### Performance

| Best Case     | Worst Case    | Average Case |
| :-------------: |:-------------:| :-----:|
| O(n)     | O(n<sup>2</sup>) | O(n<sup>2</sup>) |
| Array is already sorted. Each element being inserted into sorted portion need only be compared with element on its left.| Array is in reverse order. Each element being inserted into sorted portion must compare against every element already in the sorted portion.||

###### View example [here](https://github.com/iffig/SortingAlgorithms/blob/master/Visual%20Examples/InsertionSort.png).

*Note: I have implemented an in-place insertion sort.*

## Mergesort 

###### How It Works
Mergesort is a recursive method of sorting. To begin you split the array to be sorted in half, do this continually until you are left with n sub-arrays of size 1 (*where n is the length of the original array*). Next, merge the sub-arrays such that the newly merged lists are in order. Continue merging until you have the final sorted list of size n. 

###### Pseudocode 

```
  MergeSort(array)
    if(n > 1)
      left = MergeSort(array[1: n/2])
      right = MergeSort(array[(n/2)-1: n])
      merge(left, right)
```

###### Performance

| Best Case     | Worst Case    | Average Case |
| :-------------: |:-------------:| :-----:|
| O(n log*n*)     | O(n log*n*)  | O(n log*n*)  |

The performance of mergesort is not dependent upon how the data is ordered, it is dependent upon the size of the array being sorted. This is why the performance is the same for best, worst, and average cases. 

###### View example [here](https://github.com/iffig/SortingAlgorithms/blob/master/Visual%20Examples/MergeSort.png).


## Quicksort 

###### How It Works
Quicksort is another recursive method of sorting. For this method you pick a pivot element, in this case I have simply chosen the last element of the array to be the pivot. Each element in the array/sub-array, is compared against the pivot. If it is less than the pivot it is put below a partition/division index. After each element is sorted into the correct section, the pivot is put in the middle of the elements less than, and the elements greater than it, ensuring it is in it's sorted position. Quicksort is then called on the sub-arrays less than and greater than the pivot until everything is in sorted order. 

###### Pseudocode 

```
  QuickSort(array)
    if(1 < n)
      pivot = array[n-1]
      // Partitioning/division
      j = 0 
      for element in array
        if element < pivot 
          swap(array[j], element)
          j++
      QuickSort(array[0:j)
      QuickSort(array[j+1:n])
```

###### Performance

| Best Case     | Worst Case    | Average Case |
| :-------------: |:-------------:| :-----:|
| O(n log*n*) | O(n<sup>2</sup>) | O(n log*n*)  |
| The pivot is chosen such that the array is always split into two event sub-arrays of size n/2 (*where n is the size of the original array*). Performance is similar to mergesort.|The pivot is chosen such that the pivot is always the largest or smallest element in the sub-array, so size only decreases by 1 element each time.||


###### View example [here](https://github.com/iffig/SortingAlgorithms/blob/master/Visual%20Examples/QuickSort.png).
