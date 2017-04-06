function findMissingLetter(array){
  // creating a list with all the letters from an specific range
  //in this case, the first and last items from the array
  list_letters = []
  for (i = array[0].charCodeAt(0); i <= array[array.length - 1].charCodeAt(0); i++){
    list_letters.push(String.fromCharCode(i));
  }

  console.log("")
  console.log(array);
  console.log(list_letters);

  //checking what is the letter missing in the array
  //the first and last letter of the array are garanted to not be the one
  for (i = 1; i < list_letters.length - 1; i++){
    if (array[i] != list_letters[i]){
      return list_letters[i];
    }
  }

  return "A mistaken has happen...";

}

console.log(findMissingLetter(['a','b','c','d','f']));
console.log(findMissingLetter(['O','Q','R','S']));
