function addZero(arr) {
  let left = 0; // 배열의 앞에서부터 서칭
  let right = arr.length - 1; // 배열의 끝에서부터 서칭
  while (left < right) {
    let sum = arr[left] + arr[right];
    if (sum === 0) {
      return [arr[left] + arr[right]];
    } else if (sum > 0) {
      right--;
    } else {
      left++;
    }
  }
}
// 연산 속도를 O(N)으로 바꾼 것이 인상적이다
// Naive 접근 방법으로는 반드시 O(N^2) 가 나오는데, 연산 속도 개선에 대한 의지가 보이는 알고리즘이다.
console.log(addZero([1, 2, 3, 4, 5, 0, -1, -5, -3, -4, -2]));
