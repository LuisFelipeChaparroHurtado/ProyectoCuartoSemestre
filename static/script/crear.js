
const iconoCrear= document.querySelector('#icono-crear');
    crear= document.querySelector('#crear');

    iconoCrear.addEventListener('click',(e) =>{

        // Alternamos estilos para el menu y body
        crear.classList.toggle('active');
        document.body.classList.toggle('opacity');

        //Alternamos su atributo 'src' para el icono del menú
        const rutaActual= e.target.getAttribute('src');

        if (rutaActual == 'https://image.flaticon.com/icons/png/512/93/93073.png'){
            e.target.setAttribute('src','https://image.flaticon.com/icons/png/512/93/93073.png');
        }else{
            e.target.setAttribute('src','https://image.flaticon.com/icons/png/512/93/93073.png');
        }
    })