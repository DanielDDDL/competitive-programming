// receive a string containing a comment
// return the given string without any vowels
function disemvowel(str) {

  var arrStr = str.split(""); //turning the given string into an array of chars
  var result = ""; //restores the chars that are not vowels

  for (var i = 0; i < arrStr.length; i++){
    if (!isVowel(arrStr[i])){ //if not a vowel...
      result += arrStr[i];    //adding it to string
    }
  }

  return result;
}

function isVowel(currentChar){

  var vowels = ['a','e','i','o','u','A','E','I','O','U']
  for (i = 0; i < vowels.length; i++){
    if (currentChar == vowels[i]){
      return true;
    }
  }

  return false;
}

console.log(disemvowel("This website is for losers LOL!"));
