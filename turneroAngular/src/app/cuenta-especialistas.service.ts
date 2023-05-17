import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CuentaEspecialistasService {
  url:String= "http://localhost:3000/";
  constructor(private http:HttpClient) { }

  ObtenerUltimosMovimientos(): Observable <any>
  {
    return this.http.get(this.url+"especialistas");
  }
}
