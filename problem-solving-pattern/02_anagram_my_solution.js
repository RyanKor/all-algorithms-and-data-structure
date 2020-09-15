/*
Solving Anagram

- 똑같은 문자를 사용하지만 문자의 배열이나 위치가 바뀐 현태의 알고리즘 풀이
- 주어진 테스트 케이스의 길이를 확인하는 것도 좋지만, 여기서 중요한 것은 Frequency Count라는 점이다.
- 이전에 내가 풀 때를 생각해보면 단어를 한 개 씩 비교했던 기억이 있는데, 이를 frequency issue로 들고올 경우,
- O(N)의 연산속도 내에서 처리할 수 있다는 장점을 갖고 있다.
- 단순한 문제지만, 문제를 해결하는 관점을 어떻게 바라볼 것인가? 이에 대한 고민이 담겨야한다.
*/

function anagram(str1, str2) {
  if (str1.length !== str2.length) {
    return false;
  }
  let ana1 = {};
  for (let word = 0; word < str1.length; word++) {
    // 방법 1
    // if (ana1[str1[word]]) {
    //   ana1[str1[word]] += 1;
    // } else {
    //   ana1[str1[word]] = 1;
    // }
    // 방법 2
    ana1[str1[word]] ? (ana1[str1[word]] += 1) : (ana1[str1[word]] = 1);
  }
  for (let word = 0; word < str2.length; word++) {
    if (ana1[str2[word]]) {
      ana1[str2[word]] -= 1;
    } else {
      return false;
    }
  }
  return true;
}

console.log(anagram("nayr", "ryan"));
