/*
Multiple Pointers

Creating Pointers or Values that correspond to an index or position move forwards the beginning,
end or middle based on a certain condition

Very efficient for solving problems with minimal space complexity as well

An Example

Write a function called sumZero which accepts a sorted array of integers.
The function should find the first pari where the sum is 0.
Return an array that includes both values that sum to zero or undefined if a pair does not exist

sumZero([-3,-2,-1,0,1,2,3])
sumZero([-2,0,1,3])
sumZero([1,2,3])

*/

// [-4,-3,-2,-1,0,1,2,3,4,5]
// "alksjdalksjdlkasjdlks"

function sumZero(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === 0) {
        return [arr[i], arr[j]];
      }
    }
  }
}

console.log(sumZero([-4, -3, -2, -1, 0, 1, 2, 3, 5]));
