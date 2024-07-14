let frase = prompt("Escreva alguma cois para identificar as vogais: ");
let num = Number(prompt("Informe um valor para ter o seu valor ao quadrado: "));
let raio = Number(prompt("Digite o raio do circulo: "))

function contVogal(frase){
    let cont = 0
    const vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚãẽĩõũÃẼĨÕŨâêîôûÂÊÎÔÛ'
    for(caractere of frase){
        if(vogais.includes(caractere)){
            cont++
        }
    }
    console.log(frase)
    console.log(cont)
    alert(cont)
}

//contVogal(frase);

let quadrado = (num) => {
    let resultado = num ** 2
    alert(`O quadrado de: ${num} é ${resultado}`);
}

//quadrado(num);

function area(raio){
    let area = Math.PI * (Math.pow(raio, 2))
    let perimetro = Math.PI * (raio * 2) 
    alert(`A area do circulo é ${area} e seu perimetro ${perimetro}`)
}

area(raio)

let mult = (num1, num2) => num1 * num2
let num1 = Number(prompt("Digite um numero: "));
let num2 = Number(prompt("Digite outro numero: "));

mult(num1, num2)
alert(`A multiplicação de ${num1} e ${num2} é ${mult(num1, num2)}`)

let vogal2 = (frase) => {
    let cont = 0
    const vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚãẽĩõũÃẼĨÕŨâêîôûÂÊÎÔÛ'
    for(caractere of frase){
        if(vogais.includes(caractere)){
            cont++
        }
    }
    console.log(frase)
    console.log(cont)
    alert(cont)
}  