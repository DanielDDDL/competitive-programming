function findNb(m){
  var result = 1;
  var floor = 1;
  var isEncontrado = false;

  while (true){
    if (result == m){
      isEncontrado = true;
    } else {
      floor++;
      result += Math.pow (floor, 3);
    }

    if (isEncontrado || result > m){
      break;
    }

  }

  if (isEncontrado){
    return floor;
  } else {
    return -1;
  }

}
