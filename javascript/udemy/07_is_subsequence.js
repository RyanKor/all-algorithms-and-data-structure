/*
Multiple Pointers - isSubsequence
Write a function called isSubsequence which takes in two strings and checks whether
the characters in the first string form a subsequence of the characters in the second string.
In other words, the function should check whether the characters in the first string appear somewhere in the second string, without their order changing.

*/

function isSubsequence(str1, str2) {
  var i = 0;
  var j = 0;
  if (!str1) return true;
  while (j < str2.length) {
    if (str2[j] === str1[i]) i++; // 2개의 서로 다른 문자열, 또는 배열에 대해 2개의 포인터를 적용해서 값을 탐색하는 것이 가능하다.
    if (i === str1.length) return true;
    j++;
  }
  return false;
}

console.log(isSubsequence("hello", "hello world"));
console.log(isSubsequence("sing", "string"));
console.log(isSubsequence("abc", "abracadabra"));
console.log(isSubsequence("abc", "acb"));
