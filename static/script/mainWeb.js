const iconoMenu= document.querySelector('#icono-menu');
    menu= document.querySelector('#menu');

    iconoMenu.addEventListener('click',(e) =>{

        // Alternamos estilos para el menu y body
        menu.classList.toggle('active');
        document.body.classList.toggle('opacity');

        //Alternamos su atributo 'src' para el icono del menú
        const rutaActual= e.target.getAttribute('src');

        if (rutaActual == 'http://assets.stickpng.com/images/588a64e0d06f6719692a2d10.png'){
            e.target.setAttribute('src','http://assets.stickpng.com/images/588a64e0d06f6719692a2d10.png');
        }else{
            e.target.setAttribute('src','http://assets.stickpng.com/images/588a64e0d06f6719692a2d10.png');
        }
    })

