let produtos = JSON.parse(localStorage.getItem('produtos')) || [];
let carrinho = [];

window.onload = carregarCatalogo;

function carregarCatalogo() {
    const catalogo = document.getElementById('catalogo');
    if (!catalogo) return;
  
    catalogo.innerHTML = '';
    produtos.forEach(produto => {
      const card = document.createElement('div');
      card.classList.add('col-md-4', 'mb-4');
      card.innerHTML = `
        <div class="card">
          <img src="${produto.imagem}" class="card-img-top" alt="${produto.nome}">
          <div class="card-body">
            <h5 class="card-title">${produto.nome}</h5>
            <p class="card-text">${produto.descricao}</p>
            <p class="card-text"><strong>R$ ${produto.preco.toFixed(2)}</strong></p>
            <p class="card-text">Estoque: ${produto.estoque}</p>
            <button class="btn btn-primary" onclick="adicionarAoCarrinho(${produto.id})" ${produto.estoque === 0 ? 'disabled' : ''}>
              ${produto.estoque > 0 ? 'Adicionar ao Carrinho' : 'Sem Estoque'}
            </button>
            <button class="btn btn-danger" onclick="excluirProduto(${produto.id})">Excluir</button>
          </div>
        </div>
      `;
      catalogo.appendChild(card);
    });
}
function excluirProduto(produtoId) {
    const confirmacao = confirm('Tem certeza que deseja excluir este produto?');
    if (confirmacao) {
      produtos = produtos.filter(produto => produto.id !== produtoId);
      localStorage.setItem('produtos', JSON.stringify(produtos));
      carregarCatalogo();
      alert('Produto excluído com sucesso!');
    }
  }
  
  

  function adicionarAoCarrinho(produtoId) {
    const produto = produtos.find(p => p.id === produtoId);
    const itemCarrinho = carrinho.find(item => item.id === produtoId);
  
    if (produto.estoque > 0) {
      if (itemCarrinho) {
        itemCarrinho.quantidade++;
      } else {
        carrinho.push({ ...produto, quantidade: 1 });
      }
      produto.estoque--;
      localStorage.setItem('produtos', JSON.stringify(produtos));
      exibirCarrinho();
      carregarCatalogo();
    } else {
      alert('Produto sem estoque!');
    }
  }
  

function exibirCarrinho() {
  const carrinhoDiv = document.getElementById('carrinho');
  carrinhoDiv.innerHTML = carrinho.map(item => `
    <div class="d-flex justify-content-between">
      <span>${item.nome} (x${item.quantidade})</span>
      <span>R$ ${(item.preco * item.quantidade).toFixed(2)}</span>
    </div>
  `).join('');
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
  
    produtos.push({
      id: produtos.length + 1,
      nome,
      descricao,
      preco,
      estoque,
      imagem,
    });
  
    localStorage.setItem('produtos', JSON.stringify(produtos));
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
  