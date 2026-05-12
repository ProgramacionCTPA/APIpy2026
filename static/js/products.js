
async function load(){
let r=await fetch('/api/products/');
let d=await r.json();
let c=document.getElementById('products');
d.forEach(p=>{
c.innerHTML+=`<div class='card'><h3>${p.nombre}</h3><p>${p.precio}</p></div>`;
});
}
load();
