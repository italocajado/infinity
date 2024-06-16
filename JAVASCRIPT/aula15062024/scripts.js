function handleClick(event){
    event.preventDefault()
    
    let idade = document.getElementById("idade").value

    if(isNaN(idade)){
        alert("Por favor digite um número")
        return
    }
    // aprovado()
    // recusado()

    //Complete o código que está faltando
    // Se idade for maior que 18, chame a função aprovado()
    // caso contrário chame a função recusado()

    if(idade<18){
        recusado()
    } else{
        aprovado()
    }
}

function aprovado(){
    inserirTextoNaMensagem("Bem vindo à loja!")
    colorirMensagem("#388659")
    showMensagem()
}

function recusado() {
    inserirTextoNaMensagem("Você é de menor. Vá embora!")
    colorirMensagem("#e27396")
    showMensagem()
}

function showMensagem(){
    let $mensagem = document.getElementById("mensagem")

    $mensagem.style.display="block"

}

function inserirTextoNaMensagem(texto){
    let $mensagem = document.getElementById("mensagem")
    $mensagem.innerText=texto
}

function colorirMensagem(cor){
    let $mensagem = document.getElementById("mensagem")
    $mensagem.style.backgroundColor=cor
}