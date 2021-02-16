function anagram(str1, str2) {
  let ana = {};
  if (str1.length !== str2.length) {
    return false;
  }
  for (let i = 0; i < str1.length; i++) {
    ana[str1[i]] ? (ana[str1[i]] += 1) : (ana[str1[i]] = 1);
  }
  for (let i = 0; i < str2.length; i++) {
    if (ana[str2[i]]) {
      ana[str2[i]] -= 1;
    } else {
      return false;
    }
  }
  return true;
}

console.log(anagram("abcccc", "abcccc"));
