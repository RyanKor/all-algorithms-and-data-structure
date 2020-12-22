/*
Sliding Window

This parttern involves creating a window which can either be an array or number from one position to another.

Depending on a certain condition, the window either increases or closes (and a new window is created)

Very useful for keeping track of a subset of data in an array/string etc.


An Example

Write a function called maxSubarraySum wihch accepts an array of integers and a number called n.

The function should calculate the maximum sum of n consecutive elements in the array.

배열의 부분 합을 구하는 것은 알고리즘 문제 풀이에서 단골로 나오는 연습 문제 중 하나다.

*/

function maxSubarraySum(arr, num) {
  if (num > arr.length) {
    return null;
  }
  let max = -Infinity;
  for (let i = 0; i < arr.length - num + 1; i++) {
    temp = 0;
    for (let j = 0; j < num; j++) {
      // 이 경우, 연산속도는 반드시 O(N^2)가 나올 수 밖에 없나?
      temp += arr[i + j];
    }
    if (temp > max) {
      max = temp;
    }
    console.log(temp, max); // 여기서 이 콘솔을 찍어보는게 매우 중요한데, 그 이유는 아래의 값과 같다
    /*
    17 17
    17 17
    12 17
    11 17
    14 17
    19 19
    14 19
    */
  }

  return max;
}

console.log(maxSubarraySum([2, 6, 9, 2, 1, 8, 5, 6, 3], 3));
