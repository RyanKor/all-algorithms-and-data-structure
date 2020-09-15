function same(arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false;
  }
  let frequencyCounter1 = {}; // 객체를 활용해서 작업하는 방법. 꽤 자바스크립트스러운 답안이다.
  let frequencyCounter2 = {};
  for (let val of arr1) {
    frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1; // 갯수를 Counting하는 형태다
  }
  for (let val of arr2) {
    frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1;
  }
  console.log(frequencyCounter1);
  console.log(frequencyCounter2);
  for (let key in frequencyCounter1) {
    if (!(key ** 2 in frequencyCounter2)) {
      return false;
    }
    if (frequencyCounter2[key ** 2] !== frequencyCounter1[key]) {
      return false;
    }
  }
  return true;
}

same([1, 2, 3, 2, 5], [9, 1, 4, 4, 11]);

// 여기서 문득 생각나는 궁금증
// 사실상 연산 속도 자체는 큰 차이가 없는 것 같은데, 리팩토링한 부분이 얼마나 속도 부분에 있어서 개선을 한 것인가?
