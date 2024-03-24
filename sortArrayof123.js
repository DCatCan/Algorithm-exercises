



function solution(G){
  var t = 0
  var h = 0

  G.map((elem, index) => {
    if (elem === 1) {
      h++;
    }else{
      t++;
    }
  })
  //base cases

  //if the absolute difference is the same as the amount: t: 4 h: 0 tot: 4 => also 0
  //if t = h = m  => m coins should be turned over
  //if tot = 1 => none should be turned over

 
  if (G.length === 1 || t === 0  || h === 0) {
    return 0
  }
  if (t === h) {
    return t
  }
  return Math.min(t,h)

}

console.log(solution([1,0,0,1,0,0]))