let num1 = Number(prompt("Digite um número"))
let num2 = Number(prompt("Digite outro número"))
let opcao = Number(prompt("Escolha uma operação:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão "))


if(opcao<1 || opcao>4){
    alert("Digite uma opção entre 1 e 4")
}else{
    switch(opcao){
        case 1:
            let soma = num1 + num2
            alert(`Resultaddo: \n ${num1} + ${num2} = ${soma}`)
            break
        case 2:
            let sub = num1 - num2
            alert(`Resultaddo: \n ${num1} - ${num2} = ${sub}`)
            break
        case 3:
            let mult = num1 * num2
            alert(`Resultaddo: \n ${num1} x ${num2} = ${mult}`)
            break
        case 4:
            let divs = num1 / num2
            alert(`Resultaddo: \n ${num1} / ${num2} = ${divs}`)
            break
        default:
            alert("Digite um numero de 1 a 4!")
    }
}