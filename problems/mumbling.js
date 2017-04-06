function accum(s) {
  var result = "";
  for (i = 0; i < s.length; i++){
    result += s[i].toUpperCase();
    for (j = 0; j < i; j++){
      result += s[i].toLowerCase();
    }
    if (i != s.length - 1){
      result += "-";
    }
  }
  return result;
}
