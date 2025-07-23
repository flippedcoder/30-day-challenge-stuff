// sorts numeric datasets.
const quickSort = (dataset: number[]) => {
  // check if the dataset has more than one value.
  if (dataset.length <= 1) {
    return dataset;
  }

  // choose the pivot as the last number in the dataset.
  const pivot = dataset[dataset.length - 1];

  // two arrays for the split dataset.
  const leftSubset: number[] = [];
  const rightSubset: number[] = [];

  // loop through the dataset.
  for (let i = 0; i < dataset.length - 1; i++) {
    // this is in ascending sort order. make it > to put the values in descending order.
    if (dataset[i] < pivot) {
      leftSubset.push(dataset[i]);
    } else {
      rightSubset.push(dataset[i]);
    }
  }

  // uses recursion to loop through all of the values in each subset until each value has been sorted.
  return [...quickSort(leftSubset), pivot, ...quickSort(rightSubset)];
};

const randomDataset = [
  8293, -1205, 15093, 3120, 4139, 18743, -2561, 9402, 4843, -990, 18201, 5092,
  -2807, 6664, 1283, 13245, -1229, 16102, 7511, 3114, 4157, -842, 10202, 17483,
  -2123, 6143, 8773, 14821, -3379, 19432,
];

console.log(quickSort(randomDataset));
