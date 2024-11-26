// variables 
//variables are used to store data.. in the form of bytes, we can store string, integer, different types of data .

let name1 = 'john';    //  john is stored in name 
console.log(name1);    // for output


//Let Example 

function exampleLet() {
  let name = "Alice"; // Declaring a block-scoped variable
  console.log("Outside block:", name); // Output: Outside block: Alice

  if (true) {
      let name = "Bob"; // Different variable within this block
      console.log("Inside block:", name); // Output: Inside block: Bob
  }

  console.log("Outside block again:", name); // Output: Outside block again: Alice
}

exampleLet();



//var old method to define variables 
function exampleVar() {
  console.log("Before declaration:", x); // Output: Before declaration: undefined (hoisted)
  var x = 10; // Declaring function-scoped variable

  if (true) {
      var x = 20; // Same variable in the function
      console.log("Inside block:", x); // Output: Inside block: 20
  }

  console.log("Outside block:", x); // Output: Outside block: 20
}

exampleVar();




function exampleConst() {
  const pi = 3.14; // Declaring a constant
  console.log("The value of pi is:", pi); // Output: The value of pi is: 3.14

  // pi = 3.14159; // Error: Assignment to constant variable
}

exampleConst();
