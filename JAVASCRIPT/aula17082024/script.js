const frutas = ['manga', 'Caju', 'Caja', 'Limão']


//for(let i = 0 ; i < frutas.length; i++){
//    lista += frutas.concat()
//    console.log(lista)
//    //alert(frutas[i])
//}

const lista = document.getElementById('lista');

frutas.forEach((fruta) =>{
    lista.innerHTML += `<li>${fruta}</li>`
})

//lista = frutas.join()
//alert(lista)
//const frutas2 = ["Manga", "Caju", "Cajá", "Graviola"]
//console.log(frutas2);
//frutas2.splice(1,2,"Uva","Limão","Laranja");
//console.log(frutas2);


let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
let dobro = numeros.map((n)=>{
    return n*2
})

let ferramentas = ["MARTELO", "PREGO", "SERROTE", "RÉGUA"]

let ferramentasMin = ferramentas.map((n)=>{
    return n.toLowerCase();
})

console.log(numeros)
console.log(dobro)

console.log(ferramentas)
console.log(ferramentasMin)