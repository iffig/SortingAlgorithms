from __future__ import print_function
import sys
import random
import time
import matplotlib.pyplot as plt
import math

# --------- Insertion Sort -------------
# In Place Sorting
def insertionSort(inputArray):
    print("Performing Insertion Sort");
    print();
    returnArray = [];
    for i in range(1, len(inputArray)):
        print("Iteration " + str(i));
        print(a);
        # Keep track of element to insert
        elm = inputArray[i];
        # Find where element belongs in sorted portion
        j = i-1;
        while elm < inputArray[j] and j>=0:
            # Shift sorted portion up one index
            # This makes room for insertion
            inputArray[j+1] = inputArray[j];
            j = j-1;
        #Insert into array
        inputArray[j+1] = elm;

    print();
    print("Sorted Array");
    print(inputArray);

# Sorting using a new array
# Sorting using recursionsss

# #------ Merge Sort --------------
def merge(left, right):
    print("Merging", left, right);
    retLst = []
    while (len(left)> 0) and (len(right)> 0):
        if(left[0] > right[0]):
            retLst.append(right[0])
            right.pop(0)
        else:
            retLst.append(left[0])
            left.pop(0)

    while (len(left) > 0 and len(right) == 0):
        retLst.append(left[0])
        left.pop(0)
    while (len(right) > 0 and len(left) == 0):
        retLst.append(right[0])
        right.pop(0)
    return retLst


def mergeSort(inputArray):
    n = len(inputArray);
    returnArray = [];
    if(n <= 1):
        return inputArray;
    if (1 < n):
        # Find middle to split at
        middle = n/2;
        print("Splitting",inputArray);
        left = inputArray[0:middle];
        right = inputArray[middle:n];
        print("->", left, right);
        # Recursion!
        a = mergeSort(left);
        b = mergeSort(right);
        # Put it all back together
        returnArray = merge(a,b);
        print(" ->",returnArray);
        return returnArray;


#------ Quick Sort --------------
# Note: Quicksort using last element as pivot
def quickSort(inputArray):
    n = len(inputArray);
    if(n <= 1):
        return inputArray;
    if(1 < n):
        pivot = [inputArray[n-1]];
        print("Sorting: ", inputArray, " --> Pivot: ", pivot);
        #Items below final division are less than pivot
        division = 0;
        for i in range(0, n-1):
            if(inputArray[i] < pivot[0]):
                # If less than pivot - swap to put below division
                swap = inputArray[i];
                inputArray[i] = inputArray[division];
                inputArray[division] = swap;
                division = division+1;

        # Move pivot before division
        inputArray[n-1] = inputArray[division];
        inputArray[division] = pivot;
        print("-->",inputArray[0:division],pivot,inputArray[division+1:n]);
        # Perform quicksort on the rest
        left = quickSort(inputArray[0:division]);
        right = quickSort(inputArray[division+1:n]);
        returnArray = left + pivot + right

        return returnArray;

 #--------- Main function to run sorting --------------
def main():
    print("Please input your array - separate by spaces: ");

    arrayValues = raw_input();
    print(arrayValues)

    # Turn into array:
    arrayString = arrayValues.split(" ")
    a = [int(x) for x in arrayString]
    print(a);

    selection = "";

    # Choose sorting method
    while(selection != "q"):
        print();
        print("Choose a Sorting Algorithm: ");
        print("----------------------------");
        print("1. Insertion Sort ");
        print("2. Merge Sort");
        print("3. Quick Sort");
        print("q - quit");

        selection = raw_input();

        # Insertion Sort
        if(selection == "1"):
            insertionSort(a);
        # Merge Sort
        if(selection == "2"):
            mergedList = mergeSort(a);
        # Quick Sort
        if(selection == "3"):
            quickList = quickSort(a);
            print(quickList);

main();
