import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormGroup, Validators } from '@angular/forms';
// import { UsuarioService, Usuario } from 'src/app/services/usuario.service';
import Swal from 'sweetalert2';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css'],
  providers: [DatePipe]
})

export class RegistroComponent implements OnInit {
  form: FormGroup;
  // usuario: Usuario = new Usuario();


  constructor(private formBuilder: FormBuilder, private authService: AuthService,
    private datePipe: DatePipe, private router:Router) {
  
    this.form = this.formBuilder.group(
      {
        nombre:['',[Validators.required, Validators.minLength(3)]],
        apellido:['',[Validators.required, Validators.minLength(3)]],
        dni:['',[Validators.required, Validators.minLength(3)]],
        fechaNacimiento:['',[Validators.required]],
        password1:['',[Validators.required, Validators.minLength(3)]],
        password2:['',[Validators.required, Validators.minLength(3)]],
        email:['',[Validators.required, Validators.email]]
           })
          }

    ngOnInit():void {

           }
           campoEsValido(campo:string){

            return this.form.controls[campo].errors &&  this.form.controls[campo].touched
          
          }
          
          guardar(){
          
            if(this.form.invalid || this.repitaPassword()){
              Swal.fire({
                icon: 'error',
                title: 'Error de Inicio de Sesión',
                text: 'Revise los campos, hay errores'
              })
            }else{
              this.registro();
              Swal.fire({
                title: 'Registrando el usuario',
                html: 'Porfavor, espere. Le indicaremos cuando hayamos finalizado. ',
                didOpen: () => {
                  Swal.showLoading()
                }
              })
            }
            
          }
          
          registro() {
          
            //transformar fecha a formato regional (si no en el json llega como yyyy-mm-dd)
          //  const fechaNac1 = this.datePipe.transform(this.form.get('fechaNacimiento').value, 'dd-MM-yyyy')
          
          
            const {apellido,email,fechaNacimiento,dni,nombre,password1} = this.form.value;
          
            console.log(this.form.value)
          
            this.authService.registro(apellido,email,fechaNacimiento,dni,nombre,password1)
          
          }
          repitaPassword() {
          
          if(this.form.value["password1"] != this.form.value["password2"]  ){
           return true
          } else {
            return false
          }
          
          }
          
        
          // onEnviar(event: Event, usuario:User): void
          // {
          //   event.preventDefault;
        
          //   if (this.form.valid)
          //   {
          //     console.log("Enviando al servidor...");
          //     console.log(usuario)

          //     this.authService.onCrearUsuario(usuario).subscribe(
          //       data=>{
          //         console.log(data.id)
          //         if(data.id>0)
          //         {
          //           alert("El registro ha sido creado con exito. por favor inicie sesion");

          //           this.router.navigate(['/login']);
          //         }
          //       })
          //     }
              
          //   else
          //   {
          //     this.form.markAllAsTouched();
          //   }
        
          // };

get Password1()
          {
            return this.form.get('Password1');
          }
get Password2()
          {
            return this.form.get('Password2');
          }
get Mail()
          {
            return this.form.get('email');
          }
get Nombre()
          {
            return this.form.get('nombre');
          }
get Apellido()
          {
            return this.form.get('apellido');
          }
get FechaNacimiento()
          {
            return this.form.get('fechaNacimiento');
          }
get Dni()
          {
            return this.form.get('dni');
          }
get MailValid()
          {
            return this.Mail?.touched && !this.Mail.valid;
          }
get NombreValid()
          {
            return this.Nombre?.touched && !this.Nombre.valid;
          }
get ApellidoValid()
          {
            return this.Apellido?.touched && !this.Apellido.valid;
          }
get Password1Valid()
          {
            return this.Password1?.touched && !this.Password1.valid;
          }
get Password2Valid()
          {
            return this.Password2?.touched && !this.Password2.valid;
          }
get FechaNacimientoValid()
          {
            return this.FechaNacimiento?.touched && !this.FechaNacimiento.valid;
          }
get DniValid()
          {
            return this.Dni?.touched && !this.Dni.valid;
          }

        }



   