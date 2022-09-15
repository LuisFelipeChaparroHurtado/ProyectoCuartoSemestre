let reloj = document.getElementById("reloj");
let fechaDato= document.getElementById("fec_Datos");
let dias= ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
let meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

setInterval(function (){
    tiempo= new Date();
    hora=tiempo.getHours();
    minutos =tiempo.getMinutes();
    segundos=tiempo.getSeconds();
    dia=tiempo.getDate()
    mes=tiempo.getMonth()
    año=tiempo.getFullYear()
    m=meses[mes]
    hr=(hora>12) ? hora-12 :hora
    am=(hora>12) ? 'PM' : 'AM'

    if(hr<10){hr='0'+hr}
    if(minutos<10){minutos='0'+minutos}
    if(segundos<10){segundos='0'+segundos}
    reloj.innerHTML=hr+":"+minutos+":"+segundos+" "+am+" ";
    fechaDato.innerHTML="  "+dia+" "+m+" del "+año;
},1000)



