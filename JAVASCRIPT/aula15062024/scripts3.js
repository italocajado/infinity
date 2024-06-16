let count = Number(prompt("Digite um numero para a contagem regressiva: "))
let init = 1
let acu = 0

while(count >= 0){
    console.log('desc: ' + count)
    count--
}

while(init <= 50){
    acu += init 
    console.log(acu)
    init++
}

console.log(acu)