

function duplicates(a, n){
    var dp  = []
    var temp = []
    a.forEach((el, index) => {

        if (el !== temp[el]) {
            temp[el] = el
        }else{
            dp[el] = el
        }

    });
    console.log(dp.length === 0 ? -1 : dp.flat().join(" ").toString())
    return dp.length === 0 ? [-1] : dp.flat()

    
}

var inputArray = [3, 12, 12, 4, 12, 7, 11, 6, 5, 2, 31, 6, 12, 11]
var theLength  = inputArray.length  
console.log(duplicates(inputArray, theLength));


