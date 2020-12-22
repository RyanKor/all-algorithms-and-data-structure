// 내가 시도하고자 했던 방법

function areThereDuplicates(...args) {
  // Two pointers
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
