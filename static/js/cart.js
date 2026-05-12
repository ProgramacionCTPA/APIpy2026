async function loadCart(){
    const token = localStorage.getItem("token");

    const res = await fetch('/api/cart/',{
        headers:{
            'Authorization':'Bearer ' + token
        }
    });

    const data = await res.json();

    document.getElementById("cart").innerText =
        JSON.stringify(data, null, 2);
}

loadCart();