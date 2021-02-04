/*
거스름돈 예제

대표적으로 탐욕기법 알고리즘을 풀 때 언급되는 알고리즘 예제다.

어렵게 내려면 충분히 어렵게 낼 수 있는 문제지만, "가장 큰 순서대로" || "가장 작은 순서대로"와 같은 기준을 알게 모르게 제시한다.

문제 설명을 간단하게 하면,

당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구해라.
단, 거슬러 줘야할 돈 N은 항상 10의 배수다.
*/

//test case 1
let n = 2460
let count = 0

let coin_types = [500,100,50,10]

for (let coin=0; coin<coin_types.length; coin++){
    count += parseInt(n/coin_types[coin]) // 해당 화폐로 거슬러 줄 수 있는 동전의 갯수를 카운트하는 것
    n %= coin_types[coin]
}

console.log(count)