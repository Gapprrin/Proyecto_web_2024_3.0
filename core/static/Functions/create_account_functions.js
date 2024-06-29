

// Funciones extras

function capitalize(texto){
    let palabras = "";
    if(typeof texto === "string" && texto.trim().length > 0){
        for (const iterator of texto.split(" ")) {
            //console.log(iterator[0].toUpperCase());
            for (const letra in iterator){
                if (letra == 0){
                    palabras += iterator[letra].toUpperCase();
                }else{
                    palabras += iterator[letra].toLowerCase();
                }
            }
            palabras += " ";
        }
        return palabras.trim();
    }else{
        return;
    }
}

// listas medio raras que servirán para valdar xdd
let usuario = {
    userName: "Alfonso",
    userEmail: "acerda@gmail.com",
    userCommune: "Huechuraba",
    userPassword: "12345_R",
}


// Funciones de validación

function validarComuna(){
    let user = document.querySelector("#input-comuna");

    if(user.value > 0){
        user.classList.add("valido");
        user.classList.remove("invalido");
        document.querySelector("#error-comuna").innerHTML = "";
        console.log("true");
    }else{
        user.classList.remove("valido");
        user.classList.add("invalido");
        document.querySelector("#error-comuna").innerHTML = "Seleccione una comuna.";
    }
    // var lista_comuna = ["Alhué",
    //     "Curacaví",
    //     "María Pinto",
    //     "Melipilla",
    //     "San Pedro",
    //     "Cerrillos",
    //     "Cerro Navia",
    //     "Conchalí",
    //     "El Bosque",
    //     "Estación Central",
    //     "Huechuraba",
    //     "Independencia",
    //     "La Cisterna",
    //     "La Granja",
    //     "La Florida",
    //     "La Pintana",
    //     "La Reina",
    //     "Las Condes",
    //     "Lo Barnechea",
    //     "Lo Espejo"];
    
    // if(lista_comuna.includes(user.value.trim())){
    //     user.classList.add("valido");
    //     user.classList.remove("invalido");
    //     document.querySelector("#error-comuna").innerHTML = "";
    // }else if(user.value.trim() == ""){
    //     user.classList.remove("invalido");
    //     user.classList.remove("valido");
    //     document.querySelector("#error-comuna").innerHTML = "Debe rellenar el campo.";
    // }else{
    //     user.classList.add("invalido");
    //     user.classList.remove("valido");
    //     document.querySelector("#error-comuna").innerHTML = "No se ha encontrado la comuna.";
    // }
}


function validarNombre(){

    let user = document.querySelector("#id_username");

    if(user.value.trim().length >= 5){
        if(capitalize(user.value) == usuario.userName){
            document.querySelector("#error-usuario").innerHTML = "Nombre de usuario no disponible.";
        }else{
            user.classList.add("valido");
            user.classList.remove("invalido");
            document.querySelector("#error-usuario").innerHTML = "";
            {for (var usuario in user){
                console.log(usuario.user_name)
            }}
        }
        
    }else if(user.value.trim() == ""){
        user.classList.remove("invalido");
        user.classList.remove("valido");
        document.querySelector("#error-usuario").innerHTML = "Debe rellenar el campo.";
    }else{
        user.classList.add("invalido");
        user.classList.remove("valido");
        document.querySelector("#error-usuario").innerHTML = "Nombre de usuario inválido.";
    }
}

function validarContrasenia(){
    let user = document.querySelector("#id_password1");
    if(user.value.length >= 8){
        user.classList.add("valido");
        user.classList.remove("invalido");
        document.querySelector("#error-contrasenia").innerHTML = "";
        document.querySelector("#id_password2").removeAttribute("disabled");
    }else if(user.value == ""){
        user.classList.remove("invalido");
        user.classList.remove("valido");
        document.querySelector("#error-contrasenia").innerHTML = "Debe rellenar el campo.";
        document.querySelector("#id_password2").value = "";
        document.querySelector("#id_password2").setAttribute("disabled", "");
    }else{
        user.classList.add("invalido");
        user.classList.remove("valido");
        document.querySelector("#id_password2").setAttribute("disabled", "");
        document.querySelector("#error-contrasenia").innerHTML = "Debe tener un largo mínimo de 8 caracteres.";
    }
}


function validarRepetirContrasenia(){
    let userPass = document.querySelector("#id_password1");
    let user = document.querySelector("#id_password2");

    if(user.value == userPass.value){
        user.classList.add("valido");
        user.classList.remove("invalido");
        document.querySelector("#error-repcontrasenia").innerHTML = "";
    }else{
        user.classList.add("invalido");
        user.classList.remove("valido");
        document.querySelector("#error-repcontrasenia").innerHTML = "Las contraseñas no son iguales.";
    }
}


function validarCorreo(){
    let correo = document.querySelector("#id_email");
    if(correo.value == usuario.userEmail){
        correo.classList.add("invalido");
        correo.classList.remove("valido");
        document.querySelector("#error-correo").innerHTML = "El correo ya está en uso.";
    }else{
        correo.classList.add("valido");
        correo.classList.remove("invalido");
        document.querySelector("#error-correo").innerHTML = "";
    }
}

function validarFormulario(){
    let contrasenia = document.querySelector("#id_password1");
    let usuario = document.querySelector("#id_username");
    let comuna = document.querySelector("#input-comuna");
    let correo = document.querySelector("#id_email");
    let repcontrasenia = document.querySelector("#id_password2");
    
    if(contrasenia.classList.contains("invalido") || usuario.classList.contains("invalido") || 
    comuna.classList.contains("invalido") || correo.classList.contains("invalido") || 
    repcontrasenia.classList.contains("invalido") ){
        return false;
    }else if(contrasenia.value == "" || usuario.value == "" || 
    comuna.value == 0 || correo.value == "" || 
    repcontrasenia.value == "" ){
        comuna.classList.add("invalido")
        return false;
    }else{
        return true;
    }
}