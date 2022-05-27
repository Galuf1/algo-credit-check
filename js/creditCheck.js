exports.creditCheck = function(str) {
    const lis = str.split("")
    let ans = []
    let sum = 0
    // console.log(lis.length)

    for (let i = lis.length -1; i >= 0; i--) {
        let num = parseInt(lis[i])
        let ele = 0
        if (i % 2 === 1) {
            ele = num 
        } else {
            ele = num * 2
        }
        if (ele >= 10){
            ele = ele%10 + (ele-(ele%10))/10
            ans.push(ele)
        } else {
            ans.push(ele)
        }
        sum += ele
    } 
    if (sum%10 === 0){
        return "The number is valid!"
    } else {
        return "The number is invalid!"
    }
}
