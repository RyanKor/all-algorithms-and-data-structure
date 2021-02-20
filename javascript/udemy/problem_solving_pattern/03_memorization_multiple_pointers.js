function countUniqueValues(arr) {
  if (arr === []) return 0;
  let i = 0;

  for (let j = 1; j < arr.length; j++) {
    if (arr[i] !== arr[j]) {
      i++;
      arr[i] = arr[j]; // sorting
    }
  }
  console.log(arr);
  return i + 1;
}

console.log(countUniqueValues([1, 4, 5, 6, 7, 8, 2, 5, 6, 25]));
