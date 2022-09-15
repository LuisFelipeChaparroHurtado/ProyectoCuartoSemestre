var f = new Date();
            var hr=(f.getHours()>12) ? f.getHours()-12 : f.getHours()
            var minutos =f.getMinutes();
            var segundos =f.getSeconds();
            var am=(f.getHours()>12) ? 'PM' : 'AM'

            if(hr<10){hr='0'+hr}
            if(minutos<10){minutos='0'+minutos}
            if(segundos<10){segundos='0'+segundos}
            document.write(f.getDate() + "/" + (f.getMonth() +1) + "/" + f.getFullYear() + "   " + hr + ":" + minutos+ ":" + segundos+" "+am+".");