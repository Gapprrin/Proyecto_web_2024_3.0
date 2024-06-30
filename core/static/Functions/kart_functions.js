
let codigos_val = {"PtDRq7s0J0": 30, "TViWTzKKPB": 25, "XY2l1p85A0": 20, "ZKW8lcAm46": 15, "5GwCU5FQx5": 5, "UNXq6X04": 10};

let codigos = ["PtDRq7s0J0", "TViWTzKKPB", "XY2l1p85A0", "ZKW8lcAm46", "5GwCU5FQx5", "UNXq6X04",];

function validarCodigo(){
    let cod = document.querySelector('#input-desc-code')
    let subtotal = document.querySelector('#valor-subtotal')
    let descuento = document.querySelector('#valor-descuento')
    let total = document.querySelector('#valor-total')
    let calculo
    // let valor
    if (cod.value.trim().length > 0){
        if (codigos.includes(cod.value.trim())){
            if (subtotal.innerHTML.replace("$", "").trim() > 0){
                document.querySelector('#no_valido').innerHTML = ''
                descuento.innerHTML = codigos_val[cod.value.trim()] + '%'
                calculo = parseInt(subtotal.innerHTML.replace("$", "")) - (parseInt(subtotal.innerHTML.replace("$", "")) * (codigos_val[cod.value.trim()]/100))
                // if (calculo > 10000){
                //     descuento.innerHTML = '$' + (total - calculo)
                // }else{
                //     descuento.innerHTML = codigos_val[cod.value.trim()] + '%'
                // }
                total.innerHTML = '$' + calculo
                // valor = codigos_val[cod.value.trim()]
                document.querySelector('#input-desc-code').setAttribute('disabled', '')
            }
            return
        }
        document.querySelector('#no_valido').innerHTML = 'El código no es válido.'
        return
    }else{
        return
    }
}