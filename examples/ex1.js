
// https://github.com/Rob--W/cors-anywhere/issues/301
// https://cors-anywhere.herokuapp.com/corsdemo
function focus() {
	document.getElementById('data').focus();
}

function fn1(){

	// Variables list, Array structure
	var fruits = [ "apple", "grapes", "kiwi" , 3.1215926];
	let x = fruits.length;
	let e1 = fruits[0];

	var y = fruits.pop();
	fruits.push("mango");
	fruits.shift();
	fruits.unshift('egg');
	fruits[0] = "cow";

	var animals = new Array("lizard", "cat", "dog");
	var mixitem = ["cake", "cheese", 19.99, 45, 3.14159268];

	var person = {fn:"John", ln:"Doe", age:46, pizza:"pepperoni"};

	// Printout with values from right of equal
	document.getElementById("display1").innerHTML = fruits.length ;
	document.getElementById("display2").innerHTML = fruits.sort() ;

	// Constructing ul string in loop
	var ele = "<ul>";
	for (var key in person) {
		var k = key.toString();
		var v = person[key].toString();
		ele += "<li>" + k + " " + v + "</li>";
		
	  }
	ele+= "</ul>";
	// Print out the values
	document.getElementById("display3").innerHTML = ele;
}

/* ****************************************************** */
var e = "";
function fn2() {
	var gitems;
	gitems = ["water", "banana cake", "coffie", "milk"];
	e = "<ul>";
	gitems.forEach(fn3);
	e += "</ul>";
}
// foreach goes into this function
function fn3(value) {
	e += "<li>" + value + "</li>";
	document.getElementById("display4").innerHTML = e;
}
/* ****************************************************** */

function fn4() {
	var person = {fn:"John", ln:"Doe", age:156};
	var tags = "<ul>";
	for (let [key, value] of Object.entries(person)) {
		tags+= "<li>" + key + " " +  value + "</li>";
	}
	tags+="</ul>";
	document.getElementById("display5").innerHTML = tags ;
}
/* ****************************************************** */

function fn5() {
	var grade = parseInt(document.getElementById('data').value.toString().trim());
	if ( grade >= 90 ) {
		document.getElementById('display6').innerHTML = "A";
	}
	else if ( grade >= 80) {
		document.getElementById('display6').innerHTML = "B";
	} 
	else if ( grade >= 70) {
		document.getElementById('display6').innerHTML = "C";
	} 
	else if ( grade >= 60) {
		document.getElementById('display6').innerHTML = "D";
	}
	else {
		document.getElementById('display6').innerHTML = "F";
	}
}
/* ****************************************************** */
