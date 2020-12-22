const readline = require('readline');
const rl = readline.createInterface({ 
	input: process.stdin,
	output: process.stdout 
}); 
let input = [];
rl.on('line', function (line) { 
	input.push(line.split('').map((el) => parseInt(el))) 
    
}) 
.on('close', function () {
    input[1].sort() // 입력이 다 되고 나서, close할 때 확인하자.
    let first = input[1][input[0][0]-1]
    let second = input[1][input[0][0]-2]

    let count = parseInt(input[0][1] / (input[0][2]+1)) * input[0][2]
    count += input[0][1] % (input[0][2] + 1)
    
    let result = 0
    result += (count) * first
    result += (input[0][1] - count) * second
	console.log(result); 
	process.exit();
}); 