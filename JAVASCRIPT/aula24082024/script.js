//let pessoas =  ['Mateus','Marcos','Lucas','João','Judas','Pedro']
//
////1
//let join = pessoas.join('-')
//console.log(join)
//
////2
//let mapa = pessoas.slice(0,3);
//let mapaString = mapa.join('-') 
//console.log(mapaString)
//
////3
//pessoas.splice(4,1, 'Paulo')
//console.log(pessoas.join('-'))
//
//const listaPessoas = document.getElementById('pessoas') 
//pessoas.forEach((filtro)=>{
//    listaPessoas.innerHTML += `<li>${filtro}</li>`
//})

let pessoas = [
    {
    nome:'Italo',
    idade: 26,
},
{
    nome:'João',
    idade: 25,
},
{
    nome:'Pedro',
    idade: 30,
},
{
    nome:'Mateus',
    idade: 28,
}
]

//pessoas.forEach((p)=>{
//    console.log(`nome: ${p.nome}`)
//    console.log(`idade: ${p.idade}`)
//    console.log('------------------------')
//})
//
//let pessoasFiltro = pessoas.filter((p) =>{
//    return (p.nome[0] == 'M')
//})
//
//console.log(pessoasFiltro)

let pessoasJSON = JSON.stringify(pessoas)
let pessoasOBJ = JSON.parse(pessoasJSON)
console.log(pessoas)
console.log(pessoasJSON)
console.log(pessoasOBJ)  //retorna um objeto

let livros = [{
    nome: 'Morte no buraco negro e outros dilemas cosmicos',
    autor: 'Neil Degrasse Tyson',
    ano: '2020',
    chaves: ['Morte', 'buraco negro', 'espaço', 'astronomia']
}]

let livrosJSON = JSON.stringify(livros)
console.log(livrosJSON)
console.log(typeof(livrosJSON));