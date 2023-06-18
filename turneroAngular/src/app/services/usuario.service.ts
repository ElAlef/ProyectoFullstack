import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export class Usuario
{
  nombre:string="";
  apellido:string="";
  dni:string="";
  fechaNacimiento:string="";
  password:string="";
  email:string="";
  id:number=0;
}

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  url="http://127.0.0.1:8000/auth/registro/";

  constructor(private http:HttpClient) {
    console.log("Servicio Usuarios está corriendo");
   }

   onCrearUsuario(usuario:Usuario):Observable<Usuario> {
    return this.http.post<Usuario>(this.url, usuario);
   }
}
