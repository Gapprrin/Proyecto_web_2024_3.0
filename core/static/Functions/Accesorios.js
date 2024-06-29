function productosget() {
    // variable con url
    let url = "https://api.escuelajs.co/api/v1/products/"
    // pide informacion a url

    fetch(url)
        .then(respuesta => {
            if (!respuesta.ok) { throw new Error("error para conseguir datos") }

            return respuesta.json();

        })
        .then(datos => {
            console.log(datos)
            let titulo = datos.title;
            for (let i = 1; i < 7; i++) {
                let titulo = datos[i].title;
                let imagen = datos[i].images;
                let precio = datos[i].price;
                let descripcion = datos[i].description;

                let tituloProducto = document.getElementById(`tituloProducto${i}`);
                tituloProducto.innerHTML = titulo;

                let imagenProducto = document.getElementById(`imagen${i}`);
                imagenProducto.src = imagen;

                let precioProducto = document.getElementById(`PrecioCambiar${i}`);
                precioProducto.innerHTML = '$' +  precio;

                // let descripcionProducto = doument.getElementById(`descripcion${i}`);
                // descripcionProducto.innerHTML = descripcion;

                // let tituloProducto = document.getElementById('tituloProducto1');
                // tituloProducto.textContent = titulo;

                // let PrecioProducto = document.getElementById("PrecioCambiar");
                // PrecioProducto.textContent = precio;
            }


        }

        )
        .catch(error => {
            console.error("se produjo un error: ", error);
        })




}