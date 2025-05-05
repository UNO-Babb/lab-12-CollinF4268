# The purpose of this lab is to see the speed of different sorting techniques.
# Use the same random seed to create the same random list of nubmers for each run.
# You can change the number of elements in the arrays
# We will test 3 arrays, one that is already in order, one that is sorted in reverse order, and one that it random.

import time
import random
import AllSorts  # Make sure AllSorts.py is in the same directory

def time_sort(sort_function, data):
    """Returns the time taken to sort a copy of the input data using the given sort_function."""
    arr = data.copy()
    start = time.time()
    sort_function(arr)
    end = time.time()
    return round(end - start, 5)

def main():
    random.seed(2020)  # Ensures reproducibility

    numberTerms = 10000  # You can lower this to 1000 if sorting is too slow on your machine

    # Generate test lists
    orderedList = list(range(numberTerms))
    reversedList = list(reversed(range(numberTerms)))
    randomList = [random.randint(1, 10000) for _ in range(numberTerms)]

    print("Sorting {} elements using different algorithms...".format(numberTerms))

    # Store results for easy copy-paste into Report.txt
    def run_sort_group(name, func):
        print("\n" + name)
        print("Sorted: {:.5f} seconds".format(time_sort(func, orderedList)))
        print("Reversed: {:.5f} seconds".format(time_sort(func, reversedList)))
        print("Random: {:.5f} seconds".format(time_sort(func, randomList)))

    run_sort_group("Bubble Sort", AllSorts.bubbleSort)
    run_sort_group("Bubble Sort Early Exit", AllSorts.bubbleSortEarlyExit)
    run_sort_group("Selection Sort", AllSorts.selectionSort)
    run_sort_group("Insertion Sort", AllSorts.insertionSort)
    run_sort_group("Merge Sort", AllSorts.mergeSort)

    print("\nAll sorting complete. Copy the above times into Report.txt.")

if __name__ == '__main__':
    main()
