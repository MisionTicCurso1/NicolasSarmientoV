
function info(){
    let name=document.getElementById('Name').value;
    let surname=document.getElementById('Surname').value;
    let address=document.getElementById('Address').value;
    let age=document.getElementById('Age').value;
    let mail=document.getElementById('Mail').value;
    let destiny=document.getElementById('Destiny').value;
    console.log('Nombre: '+name);
    console.log('Apellidos: '+surname)
    console.log('Direccion: '+address)
    console.log('Edad: '+age)
    console.log('Mail: '+mail)
    console.log('Destino: '+destiny)

    for(var i=0; i< 6; i++){
        document.getElementsByClassName('datos')[i].value=""
    }
    
}