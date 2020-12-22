// 받아오는 숫자를 문자열로 전환해서, 두개의 테스트 케이스 숫자에서 받아오는
// 숫자의 빈도를 측정해보자.

function sameFrequency(n1, n2) {
  let strNumber1 = String(n1);
  let strNumber2 = String(n2);
  if (strNumber1.length !== strNumber2.length) return false;
  let frequencyCount = {};
  for (let i = 0; i < strNumber1.length; i++) {
    let counter = strNumber1[i];
    frequencyCount[counter]
      ? frequencyCount[counter] + 1
      : (frequencyCount[counter] = 1);
  }
  for (let i = 0; i < strNumber2.length; i++) {
    if (frequencyCount[strNumber2[i]]) {
      frequencyCount[strNumber2[i]] -= 1;
    } else {
      return false;
    }
    return true;
  }
}

//test case
sameFrequency(182, 281);
sameFrequency(34, 14);
sameFrequency(3589578, 5879385);
sameFrequency(22, 222);
