//receive an specific number
//return the numbers of persistences untill is has reach one digit
//example: 39 - 3*9 = 27; 2*7 = 14; 1*4 = 4 - 3
function persistence (num){
  var cont = 0;
  while (true){
    var num = String(num);
    if (num.length < 2){
      break;
    } else{
      cont++;
      values = num.split('');
      num = values[0];
      for (i = 1; i < values.length; i++){
        num = num * values[i];
      }
    }
  }
  return cont;

}
//--------TESTS----------
console.log(persistence(39))
console.log(persistence(10))
console.log(persistence(4))
console.log(persistence(222))
console.log(persistence(500))
console.log(persistence(1))
console.log(persistence(20))
