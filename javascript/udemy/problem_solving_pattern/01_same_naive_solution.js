/*
Frequency Count

This pattern uses objects or sets to collect values/frequencies of values

This can often avoid the need for nested loops or O(N^2) operations with arrays and strings
*/

function same(arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false; // test case 1 : 배열 길이 자체가 맞지 않은 경우, false를 반환한다.
  }
  for (let i = 0; i < arr1.length; i++) {
    let correctIndex = arr2.indexOf(arr1[i] ** 2);
    if (correctIndex === -1) {
      return false;
    }
    console.log(arr2);
    arr2.splice(correctIndex, 1);
  }
  return true;
}

same([1, 2, 3, 2], [9, 1, 4, 4]);
