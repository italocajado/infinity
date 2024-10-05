
const apiKey = '98f39b20a559acb2d73ed748634ab9c2';
const baseURL = 'https://api.themoviedb.org/3';
let currentBannerIndex = 0; // Índice do filme atualmente exibido no banner
let bannerMovies = []; // Filmes para o carrossel de banners

// Função para buscar os filmes populares
async function fetchPopularMovies() {
    const url = `${baseURL}/movie/popular?api_key=${apiKey}&language=pt-BR&page=1`;
    const response = await fetch(url);
    const data = await response.json();
    displayPopularMovies(data.results);
    startBannerCarousel(data.results);
}

// Função para exibir os filmes populares no carrossel
function displayPopularMovies(movies) {
    const movieContainer = document.getElementById('popular-movies');
    movieContainer.innerHTML = '';

    movies.forEach(movie => {
        const movieElement = document.createElement('div');
        movieElement.innerHTML = `
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}">
        `;
        movieContainer.appendChild(movieElement);
    });
}

// Função para atualizar o banner principal com um novo filme
function updateBanner(movie) {
    const banner = document.getElementById('banner');
    const bannerTitle = document.getElementById('banner-title');
    
    banner.style.backgroundImage = `url(https://image.tmdb.org/t/p/original${movie.backdrop_path})`;
    bannerTitle.textContent = movie.title;
}

// Função para iniciar o carrossel do banner
function startBannerCarousel(movies) {
    bannerMovies = movies; // Armazena os filmes que serão usados no carrossel
    updateBanner(bannerMovies[currentBannerIndex]); // Exibe o primeiro filme

    // Define um intervalo de 5 segundos para mudar o banner automaticamente
    setInterval(() => {
        currentBannerIndex = (currentBannerIndex + 1) % bannerMovies.length; // Atualiza o índice circularmente
        updateBanner(bannerMovies[currentBannerIndex]); // Atualiza o banner com o novo filme
    }, 5000); // Muda a cada 5 segundos (5000ms)
}

// Chamada para buscar filmes populares ao carregar a página
fetchPopularMovies();