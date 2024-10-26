let produtosDaApi = [];
let produtosCadastrados = [];
let carrinho = [];

// Função para carregar os produtos cadastrados do localStorage
function carregarProdutosCadastrados() {
    const produtosSalvos = localStorage.getItem('produtosCadastrados');
    if (produtosSalvos) {
        produtosCadastrados = JSON.parse(produtosSalvos);
    }
}

// Adiciona produtos ao localStorage
function salvarProdutosNoLocalStorage() {
    localStorage.setItem('produtosCadastrados', JSON.stringify(produtosCadastrados));
}

document.addEventListener('DOMContentLoaded', () => {
    carregarProdutosCadastrados(); // Carrega produtos ao iniciar
    carregarCatalogo();

    const formCadastro = document.getElementById('form-cadastro');
    if (formCadastro) {
        formCadastro.addEventListener('submit', e => {
            e.preventDefault();

            const nome = document.getElementById('nome').value;
            const descricao = document.getElementById('descricao').value;
            const preco = parseFloat(document.getElementById('preco').value);
            const estoque = parseInt(document.getElementById('estoque').value);
            const imagem = document.getElementById('imagem').value;

            if (nome && descricao && !isNaN(preco) && !isNaN(estoque) && imagem) {
                const novoProduto = {
                    id: Date.now(), // Gera um ID único
                    title: nome,
                    description: descricao,
                    price: preco,
                    stock: estoque,
                    image: imagem,
                };

                produtosCadastrados.push(novoProduto);
                salvarProdutosNoLocalStorage(); // Salva no localStorage
                exibirProdutos(); // Exibe produtos após o cadastro
                alert('Produto cadastrado com sucesso!');
                formCadastro.reset(); // Limpa o formulário
            } else {
                alert('Preencha todos os campos corretamente.');
            }
        });
    }
});

async function carregarCatalogo() {
    try {
        const response = await fetch('https://fakestoreapi.com/products');
        produtosDaApi = await response.json();
        produtosDaApi = produtosDaApi.map(produto => ({
            ...produto,
            stock: 10
        }));
    } catch (error) {
        console.error('Erro ao buscar produtos:', error);
        alert('Não foi possível carregar os produtos da API.');
    }
    exibirProdutos();
}

function exibirProdutos() {
    const catalogo = document.getElementById('catalogo');
    if (!catalogo) {
        console.error('Elemento do catálogo não encontrado.');
        return;
    }

    catalogo.innerHTML = ''; // Limpa o catálogo antes de exibir

    const todosProdutos = [...produtosDaApi, ...produtosCadastrados];

    todosProdutos.forEach(produto => {
        const card = document.createElement('div');
        card.classList.add('col-md-4', 'mb-4');
        card.innerHTML = `
            <div class="card" style="height: 100%;">
                <img src="${produto.image}" class="card-img-top" alt="${produto.title}" style="height: 200px; object-fit: cover;">
                <div class="card-body">
                    <h5 class="card-title">${produto.title}</h5>
                    <p class="card-text">${produto.description}</p>
                    <p class="card-text"><strong>R$ ${produto.price.toFixed(2)}</strong></p>
                    <p class="card-text">Estoque: <span id="estoque-${produto.id}">${produto.stock}</span></p>
                    <button class="btn btn-primary" onclick="adicionarAoCarrinho(${produto.id})">Adicionar ao Carrinho</button>
                    <button class="btn btn-danger" onclick="excluirProduto(${produto.id})">Excluir</button>
                </div>
            </div>
        `;
        catalogo.appendChild(card);
    });
}

function excluirProduto(produtoId) {
    produtosCadastrados = produtosCadastrados.filter(produto => produto.id !== produtoId);
    salvarProdutosNoLocalStorage(); // Atualiza o localStorage
    exibirProdutos();
    alert('Produto excluído com sucesso!');
}

function adicionarAoCarrinho(produtoId) {
    const produto = [...produtosDaApi, ...produtosCadastrados].find(p => p.id === produtoId);
    const estoqueElemento = document.getElementById(`estoque-${produtoId}`);
    const estoqueAtual = parseInt(estoqueElemento.textContent);

    if (estoqueAtual > 0) {
        const itemCarrinho = carrinho.find(item => item.id === produtoId);
        if (itemCarrinho) {
            itemCarrinho.quantidade++;
        } else {
            carrinho.push({ ...produto, quantidade: 1 });
        }
        estoqueElemento.textContent = estoqueAtual - 1;
        exibirCarrinho();
    } else {
        alert('Produto sem estoque!');
    }
}

function exibirCarrinho() {
    const carrinhoDiv = document.getElementById('carrinho');
    if (!carrinhoDiv) return;

    const total = carrinho.reduce((acc, item) => acc + (item.price * item.quantidade), 0);
    carrinhoDiv.innerHTML = carrinho.map(item => `
        <div class="d-flex justify-content-between">
            <span>${item.title} (x${item.quantidade})</span>
            <span>R$ ${(item.price * item.quantidade).toFixed(2)}</span>
        </div>
    `).join('');
    carrinhoDiv.innerHTML += `
        <div class="d-flex justify-content-between font-weight-bold">
            <span>Total</span>
            <span>R$ ${total.toFixed(2)}</span>
        </div>
    `;
}

document.getElementById('cep')?.addEventListener('blur', () => {
    const cep = document.getElementById('cep').value.replace(/\D/g, '');
    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(response => response.json())
        .then(data => {
            if (!data.erro) {
                document.getElementById('rua').value = data.logradouro || '';
                document.getElementById('bairro').value = data.bairro || '';
                document.getElementById('cidade').value = data.localidade || '';
            } else {
                alert('CEP não encontrado!');
            }
        });
});

document.getElementById('form-cadastro')?.addEventListener('submit', e => {
    e.preventDefault();

    const nome = document.getElementById('nome').value;
    const descricao = document.getElementById('descricao').value;
    const preco = parseFloat(document.getElementById('preco').value);
    const estoque = parseInt(document.getElementById('estoque').value);
    const imagem = document.getElementById('imagem').value;

    const novoProduto = {
        id: produtosCadastrados.length + produtosDaApi.length + 1, 
        title: nome,
        description: descricao,
        price: preco,
        stock: estoque,
        image: imagem,
    };

    produtosCadastrados.push(novoProduto);
    carregarCatalogo();
    alert('Produto cadastrado!');
});

function mostrarCheckout() {
    const checkout = document.getElementById('checkout');
    if (checkout) {
        checkout.style.display = 'block';
    }
}

document.getElementById('form-login')?.addEventListener('submit', e => {
    e.preventDefault();
    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;

    if (usuario === 'admin' && senha === '1234') {
        alert('Login realizado com sucesso!');
        window.location.href = 'index.html';
    } else {
        alert('Usuário ou senha incorretos.');
    }
});

document.getElementById('form-checkout')?.addEventListener('submit', e => {
    e.preventDefault();

    if (carrinho.length === 0) {
        alert('Seu carrinho está vazio!');
        return;
    }

    alert('Compra finalizada com sucesso! Obrigado por comprar conosco.');
    carrinho = [];
    exibirCarrinho();
    document.getElementById('checkout').style.display = 'none';
});