import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import Swal from 'sweetalert2';

import {async, catchError, map, Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {



  // URL DEL BACK

private baseUrl: string = "http://localhost:8000/";
  private _user: { username: any; } | undefined;




           // Se inyecta HttpClient
  constructor(private http: HttpClient) { }


  // REGISTRO

  registro(apellido: string, email: string, fechaNacimiento: string, dni: string, nombre: string, password: string) {



    const url = `${ this.baseUrl}auth/registro`;
    const body = { "apellido":apellido,"email":email,"fechaNacimiento":fechaNacimiento,"dni": dni, "nombre": nombre,"password": password, "username": email };
    console.log(url);
    console.log(body);

   return this.http.post("http://localhost:8000/auth/registro/", body).subscribe(resp => {
    Swal.fire({
      icon: 'success',
      title: 'Registro Exitoso',
      text: 'Se ha registrado con éxito',
      confirmButtonText: 'ir al Login'
    }).then(
        function(){window.location.href = '/login';
     }
    )


    },err => {

      Swal.fire({
        icon: 'error',
        title: 'Error al Registrarse',
        text: err.error.message,
        footer: "Intente nuevamente"
      })
    })



    }

  }