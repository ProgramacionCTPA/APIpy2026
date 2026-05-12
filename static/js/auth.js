function checkAuth(){
    const token = localStorage.getItem("token");
    const role = localStorage.getItem("role");

    const authLinks = document.getElementById("authLinks");
    const userLinks = document.getElementById("userLinks");
    const adminLink = document.getElementById("adminLink");

    if(token){
        authLinks.style.display = "none";
        userLinks.style.display = "inline";

        if(role === "admin"){
            adminLink.style.display = "inline";
        } else {
            adminLink.style.display = "none";
        }

    } else {
        authLinks.style.display = "inline";
        userLinks.style.display = "none";
        adminLink.style.display = "none";
    }
}

function logout(){
    localStorage.clear();
    window.location = "/";
}

checkAuth();