                                                //ANIMACIONES CON JQUERY

    //ANIMACION DEL HEADER
$(document).ready(function(){                   // Probando Jquery: hasta acá todo bien, pero luego cuando lo vinculo al header no funciona,
    console.log("jquery esta funcionando")      // no me lee la animación, así que por defecto tomo el estilo del header2 para la cabezera
});                                            // en index.html

$(document).ready(function(){                  //El codigo para la barra de navegación sería este: Debería estar fija con el estilo de header 
    $(window).scroll(function(){               //por defecto, pero si se recorre el documento cambia de tamaño y toma el estilo de header2.
        if( $(this).scrollTop() > 0 ){         
            $('header').addClass('haeder2');   //Ya revise la ruta de JQuery y lo ordene en el html, corregi esos errores que me daba por 
        } else {                               //consola, pero aun asi no lo lee. Así que opte por la 'header2'.
            $('header').removeClass('haeder2');
        }
    });
});

    //ANIMACION DEL SLIDER DE LA CABEZERA
let slider = document.querySelector(".contenedor-slider");     // Este es el codigo de animación para el Slider de la cabezera, intenté
let sliderIndividual = document.querySelectorAll(".slider");   // varias maneras de hacerlo desde jquery pero al igual que en el código del  
let contador = 1;                                              // header, no logré que funcionara y finalmente éste si cumple con el efecto de  
let width = sliderIndividual[0].clientWidth;                   // slider. El problema es que no retorna al inicio para hacer el bucle infinito. 
let intervalo = 5000;                                          // Por otro lado para evitar que la transición de la última imágen a la primera 
                                                               // sea brusca volví a poner en el index repetido la primer imágen.
window.addEventListener("resize",function (){
    width = sliderIndividual[0].clientWidth;
});

setInterval(function(){
    slides();
},intervalo);

function slides() {
    slider.style.transform = "translate("+(-width*contador)+"px)";
    slider.style.transition = "transform .8s";
    contador++;

    if(contador == sliderIndividual.lenght){
        setTimeout(function(){
            slider.style.transform = "translate(0px)";
            slider.style.transition = "transform .0s";
            contador = 1;
        },500)
    };
};

//LLAMADA A LA API DE GOOGLE MAPS
const URLGET = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCJ6rIsssHG3ZKHlIht2EGOO2tvEf4Hxdg=iniciarMapa"
$("footer").prepend('<button id="btn">GET</button>');
//Escuchamos el evento click del botón agregado
$("#btn").click(() => { 
    $.get(URLGET, function iniciaraMapa(){
    let coordenadas = {lat: -34.6451188 ,lng: -58.5896727};
    let mapa = new google.maps.Map(document.getElementById('mapa'),{
        zoom: 10,
        center: coordenadas
    });
    
    let marcador = new google.maps.marcador({
        position: coordenadas,
        mapa: mapa
        });
    });
)};

//iniciaraMapa();

    // ANIMACION DEL LOGO EN LA SECCION SERVICIOS

/*proximamente.....por ahora solo le di el efecto con animate.css desde css, y solo aparece al cargarse la pagina, 
la idea es que cuando llegue a la seccion servicios se anime el logo..*/

    //    ANAMACION DEL LOGO 'INTENTO'
    
$(()=> {
    let logo2 = $("#logo2")      

    logo2.click(() =>{
        logo2.fadeIn(5000)
    });
  
});

    //INTENTO DE ANIMACION DEL SLIDER CON JQUERY, PERO ACA ESTABA USANDO OTRO FORMATO DE Html Con Divs, ul y li
/*
$(document).ready(function (){
    //buscar los elementos
    let $lis = $('li'),
        $imagenes =$lis.find('img');
        activo = 0
        cantidad = $imagenes.lenth;

    //Ocultar todas las imagenes
    $lis.hide();

    //eliminar las imagenes como elemento y añadirlas como fondo de su parent (li)
    $imagenes.each(function (index, imagen) {
        $lis.eq(index).css({
            'background-image': 'url(' + $(imagen).atrr('src') + ')',
            'background-size' : 'cover',
            'background-position' : 'center center',
            'position' : 'absolute',
        });

        $(imagen).remove();
    });

    //mostrar la primer imagen

    $lis.eq(activo).fadeIn();

})*/