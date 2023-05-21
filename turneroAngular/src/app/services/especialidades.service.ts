import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EspecialidadesService {
  url:String= "http://localhost:3000/";
  constructor(private http:HttpClient) { }

  ObtenerListaEspecialidades(): Observable <any>
  {
    return this.http.get(this.url+"especialidades");
  }
}
