let nota = prompt("Digite a hora: ")

if (nota >= 5 && nota < 12){
    alert("你根本不知道這裡寫的是什麼, Bom Dia")
} else if (nota >= 12 && nota < 18){
    alert("Boa tarde 現在")
} else{
    alert("Boa noite")
}

let senha = prompt("Digite a senha: ")

if (senha == 'admin'){
    alert("Acesso autorizado")
} else{
    alert('Acesso negado');
}

let num = prompt('Digite um numero: ')

if (num % 2 == 0) {
    alert("Positivo e par")
} else{
    alert("Impar")
}

let peso = prompt("Digite seu peso: ")
let alt = prompt("Digite sua altura: ")
let calc = (peso / (alt * alt))

if (calc < 16.9){
    alert("Abaixo do peso")
} else if(calc >= 17 && calc < 18.4){
    alert('Abaixo do peso')
}else if(calc >= 18.5 && calc < 24.9){
    alert('Peso normal')
}else if(calc >= 25 && calc < 29.9){
    alert('Acima do peso')
}else if(calc >= 30 && calc < 34.9){
    alert('Obesidade grau 1')
}else if(calc >= 35 && calc < 40){
    alert('Obesidade grau 2')
}else if(calc >= 40){
    alert('Obesidade grau 3')
}else{
    alert("Dados incorretos")
}