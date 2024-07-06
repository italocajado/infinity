let num1 = Number(prompt("Digite um número"))
let num2 = Number(prompt("Digite outro número"))
let opcao = Number(prompt("Escolha uma operação:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão "))

function soma(){
    let resultado = num1 + num2;

    return resultado   
}

function Sub(){
    let resultado = num1 - num2
    
    return resultado   
}

function Mult(){
    let resultado = num1 * num2;

    return resultado   
}

function divs(){
    let resultado = num1 / num2;

    return resultado   
}

if(opcao<1 || opcao>4){
    alert("Digite uma opção entre 1 e 4")
}else{
    switch(opcao){
        case 1:
            alert(`Resultaddo: \n ${num1} + ${num2} = ${soma()}`)
            break
        case 2:
            alert(`Resultaddo: \n ${num1} - ${num2} = ${Sub()}`)
            break
        case 3:
            alert(`Resultaddo: \n ${num1} x ${num2} = ${Mult()}`)
            break
        case 4:
            alert(`Resultaddo: \n ${num1} / ${num2} = ${divs()}`)
            break
        default:
            alert("Digite um numero de 1 a 4!")
    }
}

