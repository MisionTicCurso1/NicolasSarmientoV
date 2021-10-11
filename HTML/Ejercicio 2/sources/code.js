
var names=['Mikasa', 'Armin','Annie','Eren','Reiner','Levi'];



function lista(names){
    let personajes=document.getElementById("personajes");
    names.forEach(n=> {
        let nomb=document.createElement('div');
        nomb.innerText=n;
        let img=document.createElement('img');
        if(n=='Mikasa'){
            img.src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fstatic.zerochan.net%2FMikasa.Ackerman.full.1730465.jpg&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(n=='Armin'){
            img.src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimg2.wikia.nocookie.net%2F__cb20140222224658%2Fshingeki-no-kyojin%2Fes%2Fimages%2Fe%2Fe8%2FArmin_Arlert.png&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(n=='Annie'){
            img.src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.absoluteanime.com%2Fattack_on_titan%2Fannie.png&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(n=='Eren'){
            img.src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.anime-planet.com%2Fimages%2Fcharacters%2Feren-yeager-23863.jpg%3Ft%3D1538658772&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(n=='Reiner'){
            img.src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fantagonisten%2Fimages%2Ff%2Ff1%2FReiner_Braun_(Anime).png%2Frevision%2Flatest%3Fcb%3D20180830012054%26path-prefix%3Dde&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(n=='Levi'){
            img.src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.nicepng.com%2Fpng%2Fdetail%2F132-1329861_pin-by-oompachan-on-aot-levi-ackerman.png&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
    
        nomb.style.display='flex';
        nomb.style.flex='auto'
        nomb.style.justifyContent='center';
        nomb.style.alignItems='center';
        nomb.appendChild(img);
        personajes.appendChild(nomb);
    });
    
    
}

function itemrandom(names){
    let len=names.length;
    let random=Math.floor(Math.random()*len)
    let nomb=document.createElement('div');
        nomb.innerText=names[random];
        let img=document.createElement('img');
        if(names[random]=='Mikasa'){
            img.src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fstatic.zerochan.net%2FMikasa.Ackerman.full.1730465.jpg&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(names[random]=='Armin'){
            img.src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimg2.wikia.nocookie.net%2F__cb20140222224658%2Fshingeki-no-kyojin%2Fes%2Fimages%2Fe%2Fe8%2FArmin_Arlert.png&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(names[random]=='Annie'){
            img.src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.absoluteanime.com%2Fattack_on_titan%2Fannie.png&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(names[random]=='Eren'){
            img.src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.anime-planet.com%2Fimages%2Fcharacters%2Feren-yeager-23863.jpg%3Ft%3D1538658772&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(names[random]=='Reiner'){
            img.src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fantagonisten%2Fimages%2Ff%2Ff1%2FReiner_Braun_(Anime).png%2Frevision%2Flatest%3Fcb%3D20180830012054%26path-prefix%3Dde&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
        if(names[random]=='Levi'){
            img.src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.nicepng.com%2Fpng%2Fdetail%2F132-1329861_pin-by-oompachan-on-aot-levi-ackerman.png&f=1&nofb=1";
            img.width=100;
            img.height=150;
        }
    
        nomb.style.display='flex';
        nomb.style.flex='auto'
        nomb.style.justifyContent='center';
        nomb.style.alignItems='center';
        nomb.appendChild(img);
        let personajes=document.getElementById("personajes")
        personajes.appendChild(nomb)
        
}



