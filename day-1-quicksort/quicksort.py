from typing import List

# sorts numeric datasets.
def quickSort(dataset: List[int]) -> List[int]:
    # check if the dataset has more than one value.
    if len(dataset) <= 1:
        return dataset
    
    # choose the pivot as the last number in the dataset.
    pivot = dataset[len(dataset) - 1]

    # two arrays for the split dataset.
    leftSubset = []
    rightSubset = []

    # loop through the dataset.
    for i in range(len(dataset) - 1):
        # this is in ascending sort order. make it > to put the values in descending order.
        if dataset[i] < pivot:
            leftSubset.append(dataset[i])
        else:
            rightSubset.append(dataset[i])

    # uses recursion to loop through all of the values in each subset until each value has been sorted.
    return [*quickSort(leftSubset), pivot, *quickSort(rightSubset)]

randomDataset = [
  8293, -1205, 15093, 3120, 4139, 18743, -2561, 9402, 4843, -990, 18201, 5092,
  -2807, 6664, 1283, 13245, -1229, 16102, 7511, 3114, 4157, -842, 10202, 17483,
  -2123, 6143, 8773, 14821, -3379, 19432,
]

print(quickSort(randomDataset))