
const formulario = document.getElementById('formulario')
const username = document.getElementById ('username')
const useremail = document.getElementById('useremail')

const Alertsuccess = document.getElementById('Alertsuccess')
const alertName = document.getElementById('alertName')
const alertEmail = document.getElementById('alertEmail')

const regusername = /^[A-Za-zÑñÁáÉéÍíÓóÚúÜü\s]+$/;
const reguseremail = /^[a-z0-9]+(\.[_a-z0-9]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,15})$/;

const pintarMensajeExito = () =>{
Alertsuccess.classList.remove('d-none')
Alertsuccess.textContent = "Formulario enviado con Éxito"

}
const pintarMensajeError = (errores) => {

errores.forEach(item =>{
  item.tipo.classList.remove("d-none")
  item.tipo.textContent = item.msg
  

})
  
}

formulario.addEventListener('submit' , e =>{
    e.preventDefault();

    console.log(username.value);
    console.log(useremail.value);

    Alertsuccess.classList.add("d-none");

    const errores = [];
    //esto devuelve true si existe solo espacios
    //console.log(!username.value.trim())

    if(!regusername.test(username.value) || !username.value.trim()){
      username.classList.add("is-invalid")
        errores.push({
          tipo: alertName,
          msg: "Formato no válido en el campo nombre, solo letras"
        })
    }else{
      username.classList.remove("is-invalid")
      username.classList.add("is-valid")
      alertName.classList.add('d-none')

    }
    if(!reguseremail.test(useremail.value) || !useremail.value.trim()){
      useremail.classList.add("is-invalid")
      errores.push({
        tipo: alertEmail,
        msg: "Escriba un correo válido"
      })
    }else{
      useremail.classList.remove("is-invalid")
      useremail.classList.add("is-valid")
      alertEmail.classList.add('d-none')

    }
    if(errores.length !== 0){
      pintarMensajeError(errores)
      return
    }
   console.log('formulario enviado');
   pintarMensajeExito();
});

  