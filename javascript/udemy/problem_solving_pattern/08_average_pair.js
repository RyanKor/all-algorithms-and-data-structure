function averagePair(arr, target) {
  // add whatever parameters you deem necessary - good luck!
  let left = 0;
  let right = arr.length - 1;
  let temp = 0;
  if (arr === []) {
    return false;
  }
  while (left < right) {
    temp = (arr[left] + arr[right]) / 2;
    if (temp == target) return true;
    if (temp < target) {
      left = left + 1;
      continue;
    }
    right = right - 1;
  }
  return false;
}
