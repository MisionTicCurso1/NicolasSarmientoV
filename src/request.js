var currentpag='https://rickandmortyapi.com/api/character'
var nextpage='https://rickandmortyapi.com/api/character'
var prevpage='https://rickandmortyapi.com/api/character'

function showall(){
    let msg=document.getElementById('text');
    let loader=document.getElementById('load');
    msg.style.display='none';
    loader.style.display='flex';

    let msgbox=document.getElementById('msgbox');
    let bgcont=document.getElementById('bgcontainer');

    let container=document.getElementById("container");
    container.innerHTML='';
    fetch(currentpag, {method:"GET"})
        .then((ans)=>{
            return ans.json();
        })
        .then((data)=>{ 
            
            cards(data);
            msgbox.style.display='none';
            bgcont.style.display='block';
            if(data.info.next===null){}
            else{
                nextpage=data.info.next;
            };
            if(data.info.prev===null){}
            else{
                prevpage=data.info.prev
            };
        })
        .catch((err)=>{
            console.log('error', err)
        })
};

function showramdom(){
    let msg=document.getElementById('text');
    let loader=document.getElementById('load');
    let msgbox=document.getElementById('msgbox');
    msgbox.style.display='flex';
    msg.style.display='none';
    loader.style.display='flex';

    let bgcont=document.getElementById('bgcontainer');
    let container=document.getElementById("container");
    container.innerHTML='';
    var random=Math.floor(Math.random()*34);
    random=String(random);
    var url='https://rickandmortyapi.com/api/character/?page='+random;
    fetch(url, {method:"GET"})
        .then((ans)=>{
            return ans.json();
        })
        .then((data)=>{ 
            console.log(data);
            cards(data);
            msgbox.style.display='none';
            bgcont.style.display='block';
            if(data.info.next===null){}
            else{
                nextpage=data.info.next;
            };
            if(data.info.prev===null){}
            else{
                prevpage=data.info.prev
            };
        })
        .catch((err)=>{
            console.log('error', err)
        });
};

function shownext(){
    let loader=document.getElementById('load');
    let msgbox=document.getElementById('msgbox');
    msgbox.style.display='flex';
    loader.style.display='flex';

    let bgcont=document.getElementById('bgcontainer');
    let container=document.getElementById("container");
    container.innerHTML='';
    fetch(nextpage, {method:"GET"})
        .then((ans)=>{
            return ans.json();
        })
        .then((data)=>{ 
            console.log(data);
            cards(data);
            msgbox.style.display='none';
            bgcont.style.display='block';
            if(data.info.next===null){
                nextpage='https://rickandmortyapi.com/api/character';
            }
            else{
                nextpage=data.info.next;
            };
            if(data.info.prev===null){}
            else{
                prevpage=data.info.prev
            };
        })
        .catch((err)=>{
            console.log('error', err)
        })
};

function showprev(){
    let loader=document.getElementById('load');
    let msgbox=document.getElementById('msgbox');
    msgbox.style.display='flex';
    loader.style.display='flex';
    
    let bgcont=document.getElementById('bgcontainer');
    let container=document.getElementById("container");
    container.innerHTML='';
    fetch(prevpage, {method:"GET"})
        .then((ans)=>{
            return ans.json();
        })
        .then((data)=>{ 
            console.log(data);
            cards(data);

            msgbox.style.display='none';
            bgcont.style.display='block';

            nextpage=data.info.next;
            if(data.info.prev===null){}
            else{
                prevpage=data.info.prev
            };
        })
        .catch((err)=>{
            console.log('error', err)
        })
};



function cards(data){
    let content=document.getElementById('container')
        data.results.forEach(element => {
           let obj=document.createElement('div');
           let box=document.createElement('div')
           let front=document.createElement('div');
           let back=document.createElement('div');
           let title=document.createElement('h2');
           let photo=document.createElement('img');

           let name=document.createElement('h2');
           let status=document.createElement('h2');
           let especie=document.createElement('h2');
           let tipo=document.createElement('h2');
           let genero=document.createElement('h2');
           let origen=document.createElement('h2');
           let location=document.createElement('h2');
        
           name.innerText='Name: '+element.name;
           status.innerText='Status: '+element.status;
           if (element.status=='Alive'){
               status.style.color='green';
           }
           else if(element.status=='Dead'){
               status.style.color='red';
           }
           else{
                status.style.color='white';
           };
           especie.innerText='Specie: '+element.species;
           tipo.innerText='Type:  '+element.type;
           genero.innerText='Genre: '+element.gender;
           origen.innerText='Origin: '+element.origin.name;
           location.innerText='Location: '+element.location.name;

        //nombre de clases
           back.className='back';
           front.className='front';
           obj.className='object';
           box.className='contenedor';
           status.className='nomb';
           especie.className='nomb';
           tipo.className='nomb';
           genero.className='nomb';
           origen.className='nomb';
           location.className='nomb';

           photo.src=element.image;
           title.innerText=element.name;
           back.append(name, status,especie,tipo,genero,origen,location);   
           front.append(photo, title);
           obj.append(front, back);
           box.append(obj);
           content.append(box);
        })
}


// function next(data){
//     fetch(data.info.next,{method:"GET"} )
//         .then((res)=>{
//             return res.json(); 
//         })
//         .then((datos)=>{
//             cards(datos);
//         });
// }