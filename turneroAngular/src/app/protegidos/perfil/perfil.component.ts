import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Rol } from 'src/app/auth/interfaces/rol';
import { AuthService } from 'src/app/auth/services/auth.service';
 import { DateValidator } from 'src/app/auth/validator/date.validator';


import Swal from 'sweetalert2';
import { Users } from 'src/app/auth/interfaces/users';
import { ProtegidosService } from 'src/app/auth/services/protegidos.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent implements OnInit {

  idstring = localStorage.getItem('id')!
  id: number = +this.idstring //parseo a number
  rol: Rol = {
    "authority" : "SIN ROL"
  } 

usuario: Users = {
  apellido: '',
  dni: '',
  fechaNacimiento: '',
  id: 0,
  email:'',
  nombre: '',
  role:'',
}
email = localStorage.getItem('username');

actualizarPerfil: FormGroup = this.formBuilder.group({

  'nombre': ['', [Validators.required, Validators.minLength(3)] ],
  'apellido': ['', [Validators.required, Validators.minLength(3)] ],
  'email': ['', [Validators.required, Validators.minLength(3), Validators.email] ],
  'localidad': ['', [Validators.required, Validators.minLength(3)] ],
  'role' : [],
  'fechaNacimiento': [],
})


  constructor(private ProtegidosService : ProtegidosService,
              private authService: AuthService,
              private formBuilder: FormBuilder,
                 ) { }

  ngOnInit(): void {

    this.ProtegidosService.getUser(this.id)
    .subscribe( (usuario) => {
    
      this.usuario = usuario; 
      console.log("Query OK");

            console.log(this.usuario)
    
     
    }, (err) => {

     
      console.log("error")
    })
  
    this.authService.getRole().subscribe((rol => {

      this.rol.authority = rol[0].authority
      console.log(this.rol.authority)

    }))

    this.actualizarPerfil.get('fechaNacimiento')?.disable();
    this.actualizarPerfil.get('role')?.disable();

  }


  validarBlancos(){

    if(this.actualizarPerfil.controls['role'].value==undefined || ''){
      this.actualizarPerfil.controls['role'].setValue(this.rol.authority)
    }

    if(this.actualizarPerfil.controls['fechaNacimiento'].value==undefined || ''){
      this.actualizarPerfil.controls['fechaNacimiento'].setValue(this.usuario.fechaNacimiento)
    }

    if(this.actualizarPerfil.controls['nombre'].value==undefined|| ''){
      this.actualizarPerfil.controls['nombre'].setValue(this.usuario.nombre)
    }

    if(this.actualizarPerfil.controls['apellido'].value==undefined || ''){
      this.actualizarPerfil.controls['apellido'].setValue(this.usuario.apellido)
    }
    

    console.log(this.actualizarPerfil.value)
  }

  perfilActualizar(id:number){

    this.validarBlancos()

    Swal.fire({
      title: 'Actualizar Perfil',
      text: "Confirma sus nuevos datos?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, actualizar',
      cancelButtonText: 'No, dejalos como estaban'
    }).then((result) => {
      if (result.isConfirmed) {
       

        const body = this.actualizarPerfil.value;

        this.authService.actualizarPerfil(id,body).subscribe((resp)=>{
        
        alert('Actualizado OK')
        
        },(err)=>{
        
        alert('Error del servidor')
        })


      }
    })

    
  }


}
