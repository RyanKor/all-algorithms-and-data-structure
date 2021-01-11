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

function getLetter(s) {
    // Write your code here
    const first = ['a','e','i','o','u']
    const second = ['b','c','d','f','g']
    const thrid = ['h','j','k','l','m']
    const fourth = ['n','p','q','r','s', 't', 'v', 'w', 'x', 'y', 'z']
    if (first.indexOf(s[0]) !== -1){
        return "A"
    }
    if (second.indexOf(s[0]) !== -1){
        return "B"
    }
    if (thrid.indexOf(s[0]) !== -1){
        return "C"
    }
    if (fourth.indexOf(s[0]) !== -1){
        return "D"
    }
}

