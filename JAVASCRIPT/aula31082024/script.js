
// let nome = prompt('Diga seu nome')
// 
// function guardarLocal(){
//     localStorage.setItem('token', nome)
// }
// 
// guardarLocal()

// let user = {
//     id : '1',
//     name : 'Italo',
//     idade: 26
// }
// 
// let convUser = JSON.stringify(user)
// 
// function userData(){
//     localStorage.setItem('Usuario', convUser)
// }
// 
// userData()

function div(a,b){
        let result = a/b
        console.log(result)    
}

try{
    let n1 = Number(prompt('Digite um numero: '))
    let n2 = Number(prompt('Digite outro numero: '))
    div(n1,n2)
}catch(error){
    alert('error')
}
