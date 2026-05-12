async function loadMovies(){
    const res = await fetch('/api/movies/');
    const movies = await res.json();

    const container = document.getElementById("movies");

    container.innerHTML = "";

    movies.forEach(m => {
        container.innerHTML += `
            <div class="card">
                <h3>${m.titulo}</h3>
                <button onclick="buy('${m._id}')">Comprar</button>
            </div>
        `;
    });
}

async function buy(id){
    const token = localStorage.getItem("token");

    if(!token){
        alert("Debe iniciar sesión");
        window.location = "/login";
        return;
    }

    await fetch('/api/cart/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'Authorization':'Bearer ' + token
        },
        body: JSON.stringify({ item_id: id })
    });

    alert("Agregado");
}

loadMovies();