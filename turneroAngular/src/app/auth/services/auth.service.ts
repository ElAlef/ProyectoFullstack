import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import Swal from 'sweetalert2';
import { LoginResponse } from '../interfaces/login-response';
import {async, catchError, map, Observable, of } from 'rxjs';
import { Rol } from '../interfaces/rol';
import { Users } from '../interfaces/users';
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
        function(){window.location.href = '/auth/login';
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

      // LOGUEO

      login(username: string , password:string ){


        const url = `${ this.baseUrl}/login`;
        const body = { "email":username , "password":password };

       return this.http.post<LoginResponse>("http://localhost:8000/auth/login/", body).subscribe(resp => {

        localStorage.setItem('token', 'Bearer '+resp.token)
        localStorage.setItem('username', resp.username)
        localStorage.setItem('role', resp.role )
        // localStorage.setItem('id', resp.id.toString())
        Swal.fire({
          icon: 'success',
          title: 'Ingreso Exitoso',
          text: '¡Bienvenid@!',
          confirmButtonText: 'ir al Dashboard'
        }).then(

          function() {window.location.href = '/perfil';
        }
        )


        },err => {

          Swal.fire({
            icon: 'error',
            title: 'Error al Loguearse',
            text: err.error.message,
            footer: "Intente nuevamente"
          })
        })



        }


        //Validación de Token

        validarToken(): Observable<boolean> {

          let ok = true;

          const url = `${this.baseUrl}/valid`;
          const headers = new HttpHeaders()
          .set('Authorization',localStorage.getItem('token') || ''); // o String vacio.



    return this.http.get(url, { headers })
    .pipe(
      map( () => {

        return true
      }), catchError (err => of(false))
    );
}


getRole():Observable<Rol[]>{

  const url = `${this.baseUrl}/valid`;
  const headers = new HttpHeaders()
  .set('Authorization',localStorage.getItem('token') || ''); // o String vacio.

return this.http.get<Rol[]>(url, { headers })

}



getUsuarios():Observable<Users[]>{

  const url = `${ this.baseUrl}/users`;
  const headers = new HttpHeaders()
  .set('Authorization',localStorage.getItem('token') || ''); // o String vacio.

  return this.http.get<Users[]>(url, {headers})
  
}

bajaUsuario(id:number){
  //agrega 'Fecha de baja' 
    const url = `${ this.baseUrl}/users/${id}/delete`;
    const body = '';
    const headers = new HttpHeaders()
    .set('Authorization',localStorage.getItem('token') || ''); // o String vacio.
  
    return this.http.put(url, body, {headers})
  
  }

  actualizarPerfil(id:number, body:any){

    const url = `${ this.baseUrl}/users/${id}`;
    const headers = new HttpHeaders()
    .set('Authorization',localStorage.getItem('token') || ''); // o String vacio.
  
    return this.http.put(url, body, {headers})
  
    }

}