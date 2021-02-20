// power(2,0) // 1
// power(2,2) // 4
// power(2,4) // 16

// function power(n, p){
//     if (p === 0) return 1
//     return Math.pow(n,p)
// }
function power(base, exponent) {
  if (exponent === 0) return 1;
  return base * power(base, exponent - 1);
}
