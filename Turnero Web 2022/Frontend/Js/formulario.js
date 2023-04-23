
const formulario = document.getElementById('formulario')
const username = document.getElementById ('username')
const useremail = document.getElementById('useremail')
const userDni = document.getElementById ('userDni')
const userApellido = document.getElementById ('userApellido')
const userTelefono = document.getElementById ('userTelefono')
const userUsuario = document.getElementById ('userUsuario')
const userContrasena = document.getElementById ('userContrasena')
const userContrasena1 = document.getElementById ('userContrasena1')

const Alertsuccess = document.getElementById('Alertsuccess')
const alertName = document.getElementById('alertName')
const alertEmail = document.getElementById('alertEmail')
const alertDni = document.getElementById('alertDni')
const alertApellido = document.getElementById('alertApellido')
const alertTelefono = document.getElementById('alertTelefono')
const alertUsuario = document.getElementById('alertUsuario')
const alertContrasena = document.getElementById('alertContrasena')
const alertContrasena1 = document.getElementById('alertContrasena1')

const regusername = /^[A-Za-zÑñÁáÉéÍíÓóÚúÜü\s]+$/;
const reguseremail = /^[a-z0-9]+(\.[_a-z0-9]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,15})$/;
const reguserDni =/^[\d]{1,3}\.?[\d]{3,3}\.?[\d]{3,3}$/;
const reguserApellido = /^[A-Za-zÑñÁáÉéÍíÓóÚúÜü\s]+$/;
const reguserTelefono =/^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$/;
const regUsuario =/^[A-Za-zÑñÁáÉéÍíÓóÚúÜü\s]+$/;
const reguserContrasena =/^^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$/;
const reguserContrasena1 =/^^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$/;

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
    console.log(userDni.value);
    console.log(userTelefono.value);
    console.log(userApellido.value);
    console.log(userUsuario.value);
    console.log(userContrasena.value);
    console.log(userContrasena1.value);
    
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



    if(!reguserApellido.test(userApellido.value) || !userApellido.value.trim()){
      userApellido.classList.add("is-invalid")
        errores.push({
          tipo: alertApellido,
          msg: "Formato no válido en el campo Apellido, solo letras"
        })
    }else{
      userApellido.classList.remove("is-invalid")
      userApellido.classList.add("is-valid")
      alertApellido.classList.add('d-none')

    }





    if(!reguserDni.test(userDni.value) || !userDni.value.trim()){
      userDni.classList.add("is-invalid")
        errores.push({
          tipo: alertDni,
          msg: "Formato no válido en el campo DNI, solo numeros"
        })
    }else{
      userDni.classList.remove("is-invalid")
      userDni.classList.add("is-valid")
      alertDni.classList.add('d-none')

    }


    if(!reguserTelefono.test(userTelefono.value) || !userTelefono.value.trim()){
      userTelefono.classList.add("is-invalid")
        errores.push({
          tipo: alertTelefono,
          msg: "Formato no válido en el campo TELEFONO, solo numeros"
        })
    }else{
      userTelefono.classList.remove("is-invalid")
      userTelefono.classList.add("is-valid")
      alertTelefono.classList.add('d-none')

    }



    if(!regUsuario.test(userUsuario.value) || !userUsuario.value.trim()){
      userUsuario.classList.add("is-invalid")
        errores.push({
          tipo: alertUsuario,
          msg: "Formato no válido en el campo usuario"
        })
    }else{
      userUsuario.classList.remove("is-invalid")
      userUsuario.classList.add("is-valid")
      alertUsuario.classList.add('d-none')

    }
 
      // Verificamos si las constraseñas no coinciden 
      if (userContrasena.value != userContrasena1.value) {
        userContrasena.classList.add("is-invalid")
        userContrasena1.classList.add("is-invalid")
        errores.push({
          tipo: alertContrasena,
          tipo: alertContrasena1,
          msg: "contraseña no valido"
        
   
          
      }) }else {
        userContrasena.classList.remove("is-invalid")
        userContrasena1.classList.remove("is-invalid")
      userContrasena.classList.add("is-valid")
      userContrasena1.classList.add("is-valid")
      alertContrasena.classList.add('d-none')
      alertContrasena1.classList.add('d-none')
       
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

  