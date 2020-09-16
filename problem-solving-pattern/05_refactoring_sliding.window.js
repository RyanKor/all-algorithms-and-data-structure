function maxSubArraySum(arr, num) {
  let maxSum = 0;
  let tempSum = 0;

  if (arr.length < num) return null;
  for (let i = 0; i < num; i++) {
    maxSum += arr[i];
  }
  tempSum = maxSum;
  for (let i = num; i < arr.length; i++) {
    tempSum = tempSum - arr[i - num] + arr[i];
    maxSum = Math.max(maxSum, tempSum);
    console.log(tempSum, maxSum);
  }
  return maxSum;
}
console.log(maxSubArraySum([2, 6, 9, 2, 1, 8, 5, 6, 3], 3));
console.log(maxSubArraySum([3, 2, 5, 5, 7, 3, 2, 4, 6, 7, 1, 9, 12], 4));
/*
17 17
12 17
11 17
14 17
19 19
14 19
*/

/*
19 19
20 20
17 20
16 20
15 20
19 20
18 20
23 23
29 29
*/
