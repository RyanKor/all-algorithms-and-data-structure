'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowels = 'aeiouAEIOU'
    let vowel_div = ''
    let conso_div = ''
    for (let i = 0; i<s.length; i++){
        vowels.indexOf(s[i]) !== -1 ? vowel_div += s[i] : conso_div += s[i]
    }
    for (let i of vowel_div+conso_div){
        console.log(i)
    }
}

