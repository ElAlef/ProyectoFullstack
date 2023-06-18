import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Users } from '../interfaces/users';

@Injectable({
  providedIn: 'root'
})
export class ProtegidosService {

  baseUrl = "http://localhost:8000"

  constructor(private http: HttpClient) { }


  getUser(id:number): Observable<Users>{
   
    const url = `${ this.baseUrl}/${id}`;
    const headers = new HttpHeaders()
    .set('Authorization',localStorage.getItem('token') || '');
   return this.http.get<Users>(url, {headers})
  
  
  }



}
