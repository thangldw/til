/*
////////////////////////////////////
// Linking a JavaScript File
let js = "amazing";
console.log(1+2+3-4);

////////////////////////////////////
// Values and Variables
console.log("tluu");
console.log(123);

let firstName = "Tluu";

console.log(firstName);
console.log(firstName);
console.log(firstName);

// Variable name conventions
let jonas_matilda = "TL";
let $function = 19;

let person = "TLUU";
let PI = 3.141516;

let myFirstJob = "Coder";
let myCurrentJob = "Teacher";

let job1 = "programmer";
let job2 = "teacher";

console.log(myFirstJob);

// Assignment
let country = 'VN';
let continent = 'ASIA';
let population = 95.5;

console.log(country);
console.log(continent);
console.log(population);

*/

////////////////////////////////////
// Data type

/*
let javascriptIsFun = true;
console.log(javascriptIsFun);

console.log(typeof true);
console.log(typeof javascriptIsFun);
console.log(typeof 23);
console.log(typeof 'tluu');


javascriptIsFun = 'YES!';
console.log(typeof javascriptIsFun);

let month;
console.log(month);
console.log(typeof month);

month = 8;
console.log(month);
console.log(typeof month);
*/

////////////////////////////////////
// let, const and var

/*
let age = 29;
age = 30;

const birthYear = 1991;
//birthYear = 1990;

var job = 'ds';
job = 'de';

lastName = 'tluu';
console.log(lastName);
*/

////////////////////////////////////
// basic operations

// const now = 2021;
// const age1 = now - 1991;
// const age2 = now - 2020;
// console.log(age1, age2);

// console.log(age1 * 3,  age2 / 5, 3**2);

// const firstName = 'tluu';
// const lastName = 'de';
// console.log(firstName + ' ' + lastName);

// let x = 1 + 2;
// x += 3;
// x += 5;
// x++;
// x--;
// x--;
// console.log(x);

// console.log(age1 > age2);
// console.log(age2 >= 10);

// const isFullAge =  age2 >= 10;
// console.log(now - 1991 > now - 2020);

// console.log(25-10-5);
// let x, y;
// x = y = 25 - 10 - 5;
// console.log(x, y);

// const averageAge = (age1 + age2)/2;
// console.log(age1, age2, averageAge);


////////////////////////////////////
// Codeing Challenge #1

// const massMark = 78;
// const heightMark = 1.69;
// const massJohn = 92;
// const heightJohn = 1.95;

// const BMIMark = massMark / heightMark ** 2;
// const BMIJohn = massJohn / (heightJohn * heightJohn);
// const markHigherBMI = BMIMark > BMIJohn;

// console.log(BMIMark, BMIJohn, markHigherBMI);


////////////////////////////////////
// Strings and Template Literals

// const firstName = 'tluu';
// const job = 'ds';
// const birthYear = 1990;
// const year = 2022;

// const tluu = "I'm " + firstName + ', a ' + (year - birthYear) + ' year old ' + job + '!';
// console.log(tluu);

// const jonasNew = `I'm ${firstName}, a ${year - birthYear} year old ${job}!`;
// console.log(jonasNew);

// console.log(`Just a regular string...`);

// console.log('String with \n\
// multiple \n\
// lines');

// console.log(`String
// multiple
// lines`);


////////////////////////////////////
// Taking Decisions: if / else Statements

// const age = 18;

// if (age >= 18) {
//   console.log('Sarah can start driving license 🚗');
// } else {
//   const yearsLeft = 18 - age;
//   console.log(`Sarah is too young. Wait another ${yearsLeft} years :)`);
// }

// const birthYear = 2012;

// let century;
// if (birthYear <= 2000) {
//   century = 20;
// } else {
//   century = 21;
// }
// console.log(century);

////////////////////////////////////
// Coding Challenge #2

// const massMark = 78;
// const heightMark = 1.69;
// const massJohn = 92;
// const heightJohn = 1.95;

const massMark = 95;
const heightMark = 1.88;
const massJohn = 85;
const heightJohn = 1.76;

const BMIMark = massMark / heightMark ** 2;
const BMIJohn = massJohn / (heightJohn * heightJohn);
console.log(BMIMark, BMIJohn);

if (BMIMark > BMIJohn) {
  console.log(`Mark's BMI (${BMIMark}) is higher than John's (${BMIJohn})!`)
} else {
  console.log(`John's BMI (${BMIJohn}) is higher than Marks's (${BMIMark})!`)
}