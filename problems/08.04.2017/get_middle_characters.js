//returning the middle of a given string
//if the number of character is odd, return one character
//otherwise, return 2
function getMiddle(s){
  //more organized and understanble manner
  if (s.length % 2 == 0){
    return s.slice(s.length/2 - 1, s.length/2 + 1);
  } else {
    return s[(s.length - 1)/2];
  }

  //cleverer solution to the problem, code wars style
  // return s.slice(Math.ceil(s.length/2) - 1, Math.floor(s.length/2 + 1));

}

//------TESTS------
// console.log(getMiddle("4546547"));
// console.log(getMiddle("454654"));
// console.log(getMiddle("123456"));
// console.log(getMiddle("12345"));
// console.log(getMiddle("68465156dfgfhghpoi544444"));
