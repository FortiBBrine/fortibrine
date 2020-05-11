
function valid (form) {
    var login = form.name.value;
    var password = form.password.value;
    if (login == "admin" && password == "admin") {
        alert("Ты ввошел в систему");
        window.location = "https://youtube.com";          
    }
    else {
        alert("Сори чувак нельзя")
    }
}
