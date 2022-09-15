
const iconoModificar= document.querySelector('#icono-modificar');
    modificar= document.querySelector('#modificar');

    iconoModificar.addEventListener('click',(e) =>{

        // Alternamos estilos para el menu y body
        modificar.classList.toggle('active');
        document.body.classList.toggle('opacity');

        //Alternamos su atributo 'src' para el icono del menú
        const rutaActual= e.target.getAttribute('src');

        if (rutaActual == 'https://image.flaticon.com/icons/png/512/32/32355.png'){
            e.target.setAttribute('src','https://image.flaticon.com/icons/png/512/32/32355.png');
        }else{
            e.target.setAttribute('src','https://image.flaticon.com/icons/png/512/32/32355.png');
        }
    })