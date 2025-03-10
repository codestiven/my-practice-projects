/*
Write a program that prints the numbers from 1 to 20, but:

If a number is divisible by 3, print "Fizz" instead.
If a number is divisible by 5, print "Buzz" instead.
If a number is divisible by both 3 and 5, print "FizzBuzz" instead.
Otherwise, print the number.
*/

let num = []
for (let i = 1;  i <= 20; i++) {
    num.push(i)
};


function converter(enter){
    if (enter.some(x => typeof x === "string")) {
        return "hay un string en tu cadena"
    }
    return enter.map(x => 
        x % 3 === 0 && x % 5 === 0 ? "FizzBuzz" : 
        x % 3 === 0 ? "Fizz" : 
        x % 5 === 0 ? "Buzz" : x )
    

}

console.log(converter(num))


