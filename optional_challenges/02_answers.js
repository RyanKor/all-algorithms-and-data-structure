function areThereDuplicates(...args) {
  // Two pointers
  // Pointer를 활용한 이 문제에 해답이 틀린 것으로 나오는데, 답을 수정할 필요가 있다
  //   args.sort((a, b) => a > b);  //여기서 값이 틀리다고 나오는데,
  args.sort(); //이렇게 바꿔서 문자열도 알아서 정렬되게끔 해줘야하는 이슈가 있는 것 같다.
  let start = 0;
  let next = 1;
  while (next < args.length) {
    if (args[start] === args[next]) {
      return true;
    }
    start++;
    next++;
  }
  return false;
}

// Frequency Counter

// function areThereDuplicates() {
//   let collection = {};
//   for (let val in arguments) { //
//     collection[arguments[val]] = (collection[arguments[val]] || 0) + 1;
//   }
//   for (let key in collection) {
//     if (collection[key] > 1) return true;
//   }
//   return false;
// }

// One Line Solution
// function areThereDuplicates() {
//     return new Set(arguments).size !== arguments.length;
//   }
