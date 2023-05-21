const URL = "https://my-json-server.typicode.com/PatoGonzalezz/patoJson/productos"
fetch(URL)
.then(res=>res.json())
.then (data=>mostrarData(data))
.catch(error => console.log(error))

const mostrarData = data =>{
    console.log(data)
    let body =''
    for(let i = 1&&2&&3&&4&&5&&6; i<data.length;i++){
        body+=`<tr><td>Producto: ${data[i].nombre} <br><br>Descripcion: ${data[i].descripcion}</td></tr>`
    }
    document.getElementById('data').innerHTML = body   
}
