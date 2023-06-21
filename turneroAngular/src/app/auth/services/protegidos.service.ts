import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { User } from 'src/app/protegidos/interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class ProtegidosService {

  baseUrl = "http://localhost:8000/"

  constructor(private http: HttpClient) { }


  getUser(id:number): Observable<User>{
   
    const url = `${ this.baseUrl}/user/profile/`;
    const headers = new HttpHeaders()
    .set('Authorization',localStorage.getItem('token') || '');
   return this.http.get<User>(url, {headers})
  
  
  }



}
