// function solution(N) {
//   var enable_print = N % 10;
//   while (N > 0) {
//     if (enable_print == 0 && N % 10 !== 0) {
//       enable_print = 1;
//     } else if (enable_print != 0 || enable_print == 0) {
//       // 수의 나눈 몫이 1이면, 자동으로 출력된다.
//       enable_print === 0
//         ? process.stdout.write("")
//         : process.stdout.write((N % 10).toString());
//     }
//     N = Math.floor(N / 10);
//   }
// }

// // 문제에 주어진 기본 답안은
// // 1) 숫자를 뒤집었을 때와 본래 숫자가 같을 때 V
// // 2) 숫자 가운데에 0이 포함되어 있을 때, 바른 값을 출력한다
// // 3) 즉, 현재 고쳐야할 에러는 2개
// // 4) 마지막 자리 수가 0일 때
// // 5) 숫자에 0이 포함되어 있지 않을 때다. V
// solution(100);

function linearSearch(arr, target) {
  // add whatever parameters you deem necessary - good luck!
  arr.forEach(e => (e === target ? arr.indexOf(e) : -1));
}
