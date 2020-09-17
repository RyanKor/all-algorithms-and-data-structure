/*
Count Unique Values

Implement the function called Count Unique Values,

which accepts a sorted array, and count the unique values in the array.

There can be negative numbers in the array, but it will always be sorted.
*/

/*
여기서도 포인터의 개념을 차용해서, 왼쪽과 오른쪽에서 배열을 탐색하는 형태의 값을 취하고 있다.
i와 j가 왼쪽과 오른쪽에서 각 각 서칭하는 게 아니고 j가 시작하는 시점에서 i보다 한 칸 앞서 for loop를 순회하고 있다.
 i
[1,1,3,2,5,6,12,8,10] 이라 한다면
   j
이런 형태로 서칭하는 것이다.
*/

function countUniqueValues(arr) {
  if (arr === []) return 0;
  let i = 0;
  for (let j = 1; j < arr.length; j++) {
    if (arr[i] !== arr[j]) {
      i++;
      arr[i] = arr[j];
    }
  }
  return i + 1;
}

console.log(countUniqueValues([1, 2, 2, 5, 7, 7, 99]));
